# Generated by Django 3.1 on 2020-09-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0018_auto_20200915_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='author',
            field=models.CharField(default='f', max_length=20),
        ),
    ]
