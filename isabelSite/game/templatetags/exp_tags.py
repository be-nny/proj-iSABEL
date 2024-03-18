from django import template
from bs4 import BeautifulSoup
import re

from django.http import JsonResponse
from selenium import webdriver
import copy
import math

register = template.Library()


@register.simple_tag
def updateUserFromBCode(user, code):
    # code = request.GET.get("code", "0")
    return updateUserExp(user, code)


def updateUserExp(user, code):
    (exists, attributes) = getAttributes(code)
    points_to_add = calculatePointsToAdd(exists, attributes)
    if 'weight' in attributes:
        user.weight_recycled += float(attributes['weight']) / float(1000)
    user.user_xp += points_to_add
    user.save()
    return points_to_add


def calculatePointsToAdd(exists, attributes):
    if exists == "0":
        return 0
    attribute_weights = {'fair trade': 50, 'emulsifier': -10, 'United Kingdom': 15, 'preservative': -15,
                         'palm oil': -50,
                         'vegetarian': 25, 'vegan': 25, 'aluminium': 30, 'cardboard': 20, 'plastic': 15, 'meat': 10,
                         'weight': 0.25}
    points = 100
    for attribute, presence in attributes.items():
        points += attribute_weights[attribute] * presence
    return round(points)


def getAttributes(code):
    url = "https://www.barcodelookup.com/" + code

    attributes = {"fair trade": 0, "emulsifier": 0, "United Kingdom": 0, "preservative": 0, "palm oil": 0,
                  "vegetarian": 0, "vegan": 0, "aluminium": 0, "cardboard": 0, "plastic": 0, "meat": 0}
    meats = []

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    dr = webdriver.Chrome(options=chrome_options)

    dr.get(url)
    bs = BeautifulSoup(dr.page_source, "html.parser")
    result = bs.find(id="product")
    if not result is None:
        elements = result.find_all("div", class_="product-meta-data")
        name = result.find("h4")

        for element in elements:
            # checks for any of the attributes in each element of the html
            info = element.find("span", class_="product-text")
            if not info is None:
                for attribute in attributes:
                    if attribute.lower() in info.text.lower():
                        attributes[attribute] = 1

            # Checks for the weight information of the product if given
            technical = element.find("ul", id="product-attributes")
            if not technical is None:
                for i in technical:
                    if "size" in i.text.lower():
                        integer_part = re.search(r'\d+', i.text).group()
                        attributes["weight"] = int(integer_part)
                    elif "weight" not in attributes:
                        attributes["weight"] = 0
                    if "weight" in i.text.lower():
                        print(i.text, "\n")
            else:
                attributes["weight"] = 0

        return (name, attributes)

    return ("0", attributes)


@register.simple_tag
def calculateLevelAndExp(user, index):
    current_exp = copy.copy(user.user_xp)
    level = 1
    next_level_exp = expForNextLevel(level)
    while next_level_exp <= current_exp:
        current_exp -= next_level_exp
        level += 1
        next_level_exp = expForNextLevel(level)
    return (level, current_exp, next_level_exp)[index]


def expForNextLevel(current_level):
    if current_level >= 199:
        return 200000
    return round(10000 * (10.1 * math.tanh((2.65 / 100) * (current_level - 99)) + 10))


@register.simple_tag
def tempReset(user):
    user.user_xp = 0
    user.save()


@register.simple_tag
def spendXP(user, amount):
    if user.user_xp > int(amount):
        user.user_xp -= int(amount)
        user.save()
        return True
    else:
        return False
