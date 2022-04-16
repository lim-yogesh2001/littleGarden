# Generated by Django 4.0 on 2022-04-07 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products_category', '0002_product_is_popular_product_is_recently_added'),
        ('order', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=3, default=0.0, max_digits=5)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Transection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orders')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transection.payment')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_category.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]