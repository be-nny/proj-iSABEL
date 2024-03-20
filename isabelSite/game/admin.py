from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser

# Custom admin class for MyUser model
class MyAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ["email", "username",]

# Registering the MyUser model with the custom admin class
admin.site.register(MyUser, MyAdmin)

def create_game_keeper():
    try:
        user = MyUser.objects.get_by_natural_key(username="GameKeeper")
        user.is_game_keeper = True
        user.save()
    except:
        print("No 'GameKeeper' account found")

create_game_keeper()
