# Author: Merve Ipek Bal, Ben Abbot, Ellis
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class Report(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reported_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.message


# Define a custom user model inheriting from AbstractUser
class MyUser(AbstractUser):
    # Set the field to be used as the unique identifier for authentication
    USERNAME_FIELD = 'username'
    # Define the field to be used as the email field
    EMAIL_FIELD = 'email'
    # Define the fields required when creating a user
    REQUIRED_FIELDS = []

    # Custom fields for the user model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_xp = models.IntegerField(default=0)
    weight_recycled = models.FloatField(default=0)
    streak = models.IntegerField(default=0)
    temporary_xp = models.IntegerField(default=0)

    # change the directory later
    leaderboard_position = models.IntegerField(default=-1)
    longest_streak = models.IntegerField(default=0)
    golden_bins_collected = models.IntegerField(default=0)

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

    def get_reset_code(self):
        return self.reset_code

    def set_reset_code(self, new_code):
        self.reset_code = new_code

    # Define the string representation of the user
    def __str__(self):
        return self.username


class Receipt(models.Model):
    receipt_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(default="0", max_length=200)
    product_name = models.CharField(default="0", max_length=200)
    product_barcode = models.CharField(default="0", max_length=20)

    def get_product_name(self):
        return self.product_name

    def get_product_barcode(self):
        return self.product_barcode

    def __str__(self):
        return self.receipt_id
