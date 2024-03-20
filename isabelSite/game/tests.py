from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

User = get_user_model()
class TestViews(TestCase):

    def setUp(self):
        MyUser = get_user_model()
        # Retrieve MyUser objects with username starting with 'test'
        users_to_delete = MyUser.objects.filter(username__startswith='test')
        # Delete the retrieved users
        users_to_delete.delete()
        self.signup_url = reverse('signUp')
        self.reset_password_code_url = reverse('reset_password_code')
        self.reset_password_url = reverse('reset_password')
        self.scan_url = reverse('scan')
        self.exp_demo_url = reverse('exp_demo')
        self.rewards_url = reverse('rewards')
        self.leaderboard_url = reverse('leaderboard')
        self.profile_url = reverse('profile')
        self.about_url = reverse('about')
        self.users_url = reverse('users')
        self.reports_url = reverse('reports')

        self.user = MyUser.objects.create_user(username='testuser123', password='12345')

    def test_signup_view(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')


    def test_scan_view_authenticated(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(user)
        response = self.client.get(self.scan_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/scan.html')

    def test_scan_view_not_authenticated(self):
        response = self.client.get(self.scan_url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect response
        self.assertRedirects(response, '/login-signup/')

    """    def test_exp_demo_view_authenticated(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(user)
        response = self.client.get(self.exp_demo_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/expDemo.html')

    def test_exp_demo_view_not_authenticated(self):
        response = self.client.get(self.exp_demo_url)
        self.assertRedirects(response, '/login-signup/')
    """
    def test_rewards_view_authenticated(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(user)
        response = self.client.get(self.rewards_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/rewards.html')

    def test_rewards_view_not_authenticated(self):
        response = self.client.get(self.rewards_url)
        self.assertRedirects(response, '/login-signup/')

    def test_leaderboard_view_authenticated(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(user)
        response = self.client.get(self.leaderboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/leaderboard.html')

    def test_leaderboard_view_not_authenticated(self):
        response = self.client.get(self.leaderboard_url)
        self.assertRedirects(response, '/login-signup/')

    def test_profile_view_authenticated(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(user)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/profile.html')

    def test_profile_view_not_authenticated(self):
        response = self.client.get(self.profile_url)
        self.assertRedirects(response, '/login-signup/')

    def test_about_view_authenticated(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(user)
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/about.html')

    def test_about_view_not_authenticated(self):
        response = self.client.get(self.about_url)
        self.assertRedirects(response, '/login-signup/')

    def test_users_view_authenticated(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(user)
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamekeeper/users.html')

    def test_users_view_not_authenticated(self):
        response = self.client.get(self.users_url)
        self.assertRedirects(response, '/login-signup/')

    def test_reports_view_authenticated(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(user)
        response = self.client.get(self.reports_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamekeeper/reports.html')

    def test_reports_view_not_authenticated(self):
        response = self.client.get(self.reports_url)
        self.assertRedirects(response, '/login-signup/')
