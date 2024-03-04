from bs4 import BeautifulSoup
import re
from selenium import webdriver

def getAttributes(code):
    url = "https://www.barcodelookup.com/" + code

    attributes = {"fair trade": 0, "emulsifier": 0, "United Kingdom": 0, "preservative": 0, "palm oil": 0,
                  "vegetarian": 0, "vegan": 0, "aluminium": 0, "cardboard": 0, "plastic": 0, "meat": 0}
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


if __name__ == "__main__":
    codes = ["50001690304311", "5099077002265", "5060490010533", "5000169200049", "5410316966139", "5010605400339",
             "5000328015583", "4009900532037", "8711200562725", "7622210470126", "5449000000996", "0787099226947",
             "5020411121151", "5010003000131", "5051898971137", "5000159510691"]

    for code in codes:
        print(getAttributes(code))
