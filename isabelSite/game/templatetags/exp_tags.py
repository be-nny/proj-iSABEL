import logging
import random
import time

from django import template
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import re
import copy
import math

register = template.Library()


@register.simple_tag
def updateUserFromBCode(user, code):
    # code = request.GET.get("code", "0")
    return updateUserExp(user, code)


def updateUserExp(user, code):
    (name, attributes) = getAttributes(code)
    new_receipt = Receipt(username = user.username, product_name = name, product_barcode = code)
    new_receipt.save()
    points_to_add = calculatePointsToAdd(name, attributes)
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

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4899.30 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4899.30 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4899.30 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4899.30 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    ]

    chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--no-sandbox')  # Required when running as root
    dr = webdriver.Chrome(options=chrome_options)
    try:
        dr.get(url)
        try:
            # Switch to the CAPTCHA iframe
            WebDriverWait(dr, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='Widget containing a Cloudflare security challenge']")))
            # Click the "I'm not a robot" checkbox
            WebDriverWait(dr, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='ctp-checkbox-label']"))).click()
            # Wait for the CAPTCHA challenge to be resolved (adjust timeout as needed)
            WebDriverWait(dr, 10).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='g-recaptcha']")))
            time.sleep(5)
        except Exception:
            pass

        bs = BeautifulSoup(dr.page_source, "html.parser")
        dr.get_screenshot_as_file("screenshot.png")

        logging.basicConfig(level=logging.DEBUG)  # Set log level to DEBUG or higher
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
    finally:
        dr.quit()


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
