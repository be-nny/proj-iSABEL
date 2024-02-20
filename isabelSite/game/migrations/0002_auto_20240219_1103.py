# Generated by Django 3.2.23 on 2024-02-19 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='golden_bins_collected',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='leaderboard_position',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='myuser',
            name='longest_streak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='streak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='total_weight_recycled',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_xp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='weight_recycled',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]