import smtplib
from django import template
from django.core.mail import send_mail
import random



register = template.Library()

@register.simple_tag
def sendResetCode(request):
    email = request.GET.get('email', '')

    code = randomCode()
    if email != '':
        try:
            send_mail("iSABEL Password Reset Code",
                  "Here is your password reset code: " + code,
                  "from@example.com",
                  [email],
                  fail_silently=False,)
        except smtplib.SMTPException:
            print("could not send email.")
            return True
    else:
        return False
def randomCode():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))