# Generated by Django 3.1 on 2020-08-31 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0004_item_titleline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='body',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='item',
            name='userfile',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
