# Generated by Django 4.0.2 on 2022-04-26 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orders_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='product_id',
        ),
    ]