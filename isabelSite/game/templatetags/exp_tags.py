from django import template
register = template.Library()

def calculate_points_to_add(param1, param2, param3):
    param1_weight = 1
    param2_weight = 1
    param3_weight = 1
    points = (param1_weight*param1 + param2_weight*param2 + param3_weight*param3)
    return points

@register.simple_tag
def update_user_points(user):
    points_assigned = calculate_points_to_add(1, 1, 1)
    user.user_xp += points_assigned
    user.save()
    return points_assigned