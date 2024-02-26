from django import template
register = template.Library()

def calculate_points_to_add(param1, param2, param3):
    param1_weight = 1
    param2_weight = 1
    param3_weight = 1
    points = (param1_weight*int(param1) + param2_weight*int(param2) + param3_weight*int(param3))
    return points

@register.simple_tag
def update_user_exp(user, isvegan, isplastic, isheavy):
    points_assigned = calculate_points_to_add(isvegan, isplastic, isheavy)
    user.user_xp += points_assigned
    user.save()
    return points_assigned

@register.simple_tag
def update_user_exp_from_form(user, request):
    return update_user_exp(user, request.GET.get("isvegan", "0"), request.GET.get("isplastic", "0"), request.GET.get("isheavy", "0"))