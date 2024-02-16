import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    username = models.CharField(max_length=20,null=False,blank=False)
    first_name = models.CharField(max_length=20,null=False,blank=False)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    user_xp = models.IntegerField(default=0)
    weight_recycled = models.FloatField(default=0)
    streak = models.IntegerField(default=0)
    #change the directory later
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    total_weight_recycled = models.FloatField(default=0)
    leaderboard_position = models.IntegerField()
    longest_streak = models.IntegerField(default=0)
    golden_bins_collected = models.IntegerField(default=0)

    def __str__(self):
        return self.username