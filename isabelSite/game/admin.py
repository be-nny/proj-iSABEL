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
