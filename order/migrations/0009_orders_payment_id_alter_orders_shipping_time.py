# Generated by Django 4.0.2 on 2022-05-29 16:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transection', '0005_transection_status'),
        ('order', '0008_alter_orders_shipping_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transection.payment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='shipping_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 1, 42, 35, 62329), editable=False, null=True),
        ),
    ]
