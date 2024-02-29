from django import template
from django.core.mail import send_mail
from django.conf import settings

import random
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

register = template.Library()

@register.simple_tag
def sendResetCode(request):
    usr_email = request.GET.get('email', '')
    code = randomCode()

    if usr_email != '':
        message = "Here is your password reset code " + code

        subject = "Password Reset"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [usr_email, ]
        send_mail(subject, message, email_from, recipient_list)

        return True
    return False

def randomCode():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))