# Generated by Django 3.1.7 on 2021-03-02 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210302_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 15, 26, 26, 238554)),
        ),
    ]