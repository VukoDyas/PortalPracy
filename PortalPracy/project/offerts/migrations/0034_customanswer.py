# Generated by Django 2.2 on 2019-06-13 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offerts', '0033_auto_20190613_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_type', models.CharField(choices=[('T', 'text'), ('R', 'single-choice'), ('C', 'multiple-choice')], default='T', max_length=1, null=True)),
                ('answer', models.TextField(null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offerts.CustomQuestion')),
            ],
        ),
    ]
