# Generated by Django 4.0 on 2022-04-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_recently_added',
            field=models.BooleanField(default=False),
        ),
    ]
