import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Define a custom user model inheriting from AbstractUser
class MyUser(AbstractUser):
    # Set the field to be used as the unique identifier for authentication
    USERNAME_FIELD = 'username'
    # Define the field to be used as the email field
    EMAIL_FIELD = 'email'
    # Define the fields required when creating a user
    REQUIRED_FIELDS = []

    # Custom fields for the user model
    first_name = models.CharField(max_length=20, null=False, blank=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_xp = models.IntegerField(default=0)
    weight_recycled = models.FloatField(default=0)
    streak = models.IntegerField(default=0)

    # change the directory later
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    leaderboard_position = models.IntegerField(default=-1)
    longest_streak = models.IntegerField(default=0)
    golden_bins_collected = models.IntegerField(default=0)
    # is_game_keeper = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    # Define methods to retrieve user information
    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_first_name(self):
        return self.first_name

    def get_short_name(self):
        # Return first name or part of the email before '@'
        return self.first_name or self.email.split('@')[0]

    def get_user_xp(self):
        return self.user_xp

    def get_weight_recycled(self):
        return self.weight_recycled

    def get_streak(self):
        return self.streak

    def get_profile_pic(self):
        return self.profile_pic

    def get_leaderboard_position(self):
        return self.leaderboard_position

    def get_longest_streak(self):
        return self.longest_streak

    def get_golden_bins_collected(self):
        return self.golden_bins_collected

    # Define the string representation of the user
    def __str__(self):
        return self.username

# Author: Merve Ipek Bal