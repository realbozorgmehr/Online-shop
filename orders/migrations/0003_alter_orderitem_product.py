# Generated by Django 5.0.6 on 2024-05-27 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_product_price'),
        ('orders', '0002_coupon_alter_order_options_order_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='home.product'),
        ),
    ]
