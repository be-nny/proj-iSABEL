import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_game_keeper', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_game_keeper', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


# Create your models here.
class MyUser(AbstractUser):

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    first_name = models.CharField(max_length=20, null=False, blank=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_xp = models.IntegerField(default=0)
    weight_recycled = models.FloatField(default=0)
    streak = models.IntegerField(default=0)
    # change the directory later
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    total_weight_recycled = models.FloatField(default=0)
    leaderboard_position = models.IntegerField(default=-1)
    longest_streak = models.IntegerField(default=0)
    golden_bins_collected = models.IntegerField(default=0)
    # is_game_keeper = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_first_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]

    def get_user_xp(self):
        return self.user_xp

    def get_weight_recycled(self):
        return self.weight_recycled

    def get_streak(self):
        return self.streak

    def get_profile_pic(self):
        return self.profile_pic

    def get_total_weight_recycled(self):
        return self.total_weight_recycled

    def get_leaderboard_position(self):
        return self.leaderboard_position

    def get_longest_streak(self):
        return self.longest_streak

    def get_golden_bins_collected(self):
        return self.golden_bins_collected

    def __str__(self):
        return self.username
