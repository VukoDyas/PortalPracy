# Generated by Django 2.2 on 2019-04-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_in', '0003_profile_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]