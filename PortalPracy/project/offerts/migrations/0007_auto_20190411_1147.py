# Generated by Django 2.2 on 2019-04-11 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerts', '0006_auto_20190411_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offert',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offerts.Agency'),
        ),
    ]
