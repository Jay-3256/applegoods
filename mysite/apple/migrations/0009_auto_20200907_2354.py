# Generated by Django 3.1 on 2020-09-07 23:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0008_auto_20200907_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
