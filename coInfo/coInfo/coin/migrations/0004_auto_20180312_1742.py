# Generated by Django 2.0.2 on 2018-03-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0003_auto_20180312_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
