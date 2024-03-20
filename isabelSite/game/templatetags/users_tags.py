# AUTHOR: Alicia Henderson
from django import template

from ..models import Report
from ..models import MyUser

register = template.Library()

# Function for gamekeepers to delete users
@register.simple_tag
def remove(player):
    try:
        MyUser.objects.get_by_natural_key(player).delete()
    except:
        print("User not found")




