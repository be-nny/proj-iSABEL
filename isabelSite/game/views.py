from django.contrib.auth import logout
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import MyUser, Report
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST
from .templatetags.exp_tags import updateUserFromBCode, spendXP

"""
Initialises the login and sign up flow
"""
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


"""
View for the scan page, if a user isn't logged in, they are redirected
"""
def scan(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, "site/scan.html", {})


"""
View for the update page, if a user isn't logged in, they are redirected
"""
def expDemo(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, "site/expDemo.html", {})


"""
When a user isn't logged in, they are redirected to the log in and sign up page
"""
def userNotLoggedIn(request):
    logout(request)
    return render(request, "registration/login-signup.html", {})


"""
View for the login and sign up page
"""
def loginSignup(request):
    return render(request, "registration/login-signup.html", {})


"""
View for the user map page, if a user isn't logged in, they are redirected
"""
def rewards(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, "site/rewards.html", {})


"""
View for the leaderboard page, if a user isn't logged in, they are redirected
"""
def leaderboard(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        mydata = MyUser.objects.all().order_by('user_xp').values()
        template = loader.get_template('site/leaderboard.html')
        context = {
            'myusers': mydata,
        }
        return HttpResponse(template.render(context, request))


"""
View for the users profile page, if a user isn't logged in, they are redirected
"""
def profile(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, "site/profile.html", {})


"""
View for the about page, if a user isn't logged in, they are redirected
"""
def about(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, "site/about.html", {})


def update_user_from_bcode(request):
    decoded_text = request.GET.get('code', '0')
    updateUserFromBCode(request.user, decoded_text)

    # Assuming you're sending decodedText as a query parameter
    # Perform actions to update user based on decoded_text
    # Example:
    # user.update(decoded_text)
    return JsonResponse({'success': True})


def buy_voucher(request):
    amount = request.GET.get('amount', '0')
    request = spendXP(request.user, amount)
    if request:
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


"""
View for the gamekeeper page where they can view all users and their rank, if a user isn't logged in, they are redirected
"""
def users(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, 'gamekeeper/users.html', {})

    """
    View for the reports page where the gamekeeper can view reports, if a user isn't logged in, they are redirected
    """
def reports(request):
    if not request.user.is_authenticated:
        return userNotLoggedIn(request)
    else:
        return render(request, 'gamekeeper/reports.html', {})

@require_POST
def save_report(request):
    message = request.POST.get('reportInputField')
    if message != "":
        new_report = Report.objects.create(message=message)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Message is required'})