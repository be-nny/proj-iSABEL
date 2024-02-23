from django import template
register = template.Library()

def calculateAndUpdate(param1, param2, param3):
    param1_weight = 1
    param2_weight = 1
    param3_weight = 1
    points = (param1_weight*param1 + param2_weight*param2 + param3_weight*param3)
    return points

@register.simple_tag
def hello_user(name):
    return calculateAndUpdate(True, True, True)