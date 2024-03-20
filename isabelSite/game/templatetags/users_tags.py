# AUTHOR: Alicia Henderson
from django import template

from ..models import Report
from ..models import MyUser

register = template.Library()

# Function for gamekeepers to delete users
@register.simple_tag
def remove(request):
    username = request.GET.get("userInputField", "")
    if username != "":
        try:
            MyUser.objects.get_by_natural_key(username=username).delete()
        except:
            print("User not found")




