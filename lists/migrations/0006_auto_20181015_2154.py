# Generated by Django 2.1 on 2018-10-15 14:54

from django.db import migrations, models
import lists.models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20181015_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.TextField(default=None, verbose_name=lists.models.List),
        ),
    ]
