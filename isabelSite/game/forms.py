from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

# Custom form for user creation, based on UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username", "email",)

# Custom form for user change, based on UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ("username", "email",)
