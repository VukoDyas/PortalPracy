# Generated by Django 2.2 on 2019-05-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_in', '0004_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='employer',
            field=models.BooleanField(default=False),
        ),
    ]