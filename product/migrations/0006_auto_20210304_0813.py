# Generated by Django 3.1.7 on 2021-03-04 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210304_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 8, 13, 30, 80062)),
        ),
    ]