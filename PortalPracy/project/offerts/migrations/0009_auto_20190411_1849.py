# Generated by Django 2.2 on 2019-04-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerts', '0008_auto_20190411_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offert',
            name='expiration_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
