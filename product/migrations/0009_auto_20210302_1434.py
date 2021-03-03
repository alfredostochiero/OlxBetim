# Generated by Django 3.1.7 on 2021-03-02 17:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210301_1816'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'Imagem do Produto', 'verbose_name_plural': 'Imagens do Produto'},
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 2, 14, 34, 9, 43121)),
        ),
    ]