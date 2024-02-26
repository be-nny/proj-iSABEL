from django import template
from bs4 import BeautifulSoup
import re
from selenium import webdriver

register = template.Library()


@register.simple_tag
def updateUserFromBCode(user, request):
    code = request.GET.get("code", "0")
    return updateUserExp(user, code)

def updateUserExp(user, code):
    (exists, attributes) = getAttributes(code)
    points_to_add = calculatePointsToAdd(exists, attributes)
    user.user_xp += points_to_add
    user.save()
    return points_to_add

def calculatePointsToAdd(exists, attributes):
    if exists:
        attribute_weights = {'fair trade': 50, 'emulsifier': -10, 'United Kingdom': 15, 'preservative': -5, 'palm oil': -50,
                             'vegetarian': 25, 'vegan': 25, 'aluminium': 30, 'cardboard': 20, 'plastic': 10, 'meat': 10,
                             'weight': 0.5}
        points = 100
        for attribute, presence in attributes.items():
            points += attribute_weights[attribute] * presence
        return round(points)
    return 0

def getAttributes(code):
    url = "https://www.barcodelookup.com/" + code

    attributes = {"fair trade": 0, "emulsifier": 0, "United Kingdom": 0, "preservative": 0, "palm oil": 0, "vegetarian": 0, "vegan": 0, "aluminium": 0, "cardboard": 0, "plastic": 0, "meat": 0}
    meats = []

    dr = webdriver.Chrome()
    dr.get(url)
    bs = BeautifulSoup(dr.page_source, "html.parser")
    result = bs.find(id="product")
    if not result is None:
        elements = result.find_all("div", class_="product-meta-data")

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

        return (True, attributes)

    else:
        return (False, attributes)