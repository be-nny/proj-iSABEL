# Generated by Django 5.0.2 on 2024-03-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_receipt_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='temporary_xp',
            field=models.IntegerField(default=0),
        ),
    ]
