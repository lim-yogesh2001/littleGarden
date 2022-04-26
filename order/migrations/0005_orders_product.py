# Generated by Django 4.0.2 on 2022-04-26 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_category', '0005_product_price'),
        ('order', '0004_remove_orders_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products_category.product'),
        ),
    ]