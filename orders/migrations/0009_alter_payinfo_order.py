# Generated by Django 5.0.6 on 2024-05-29 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_payinfo_order_alter_payinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payinfo',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_info', to='orders.order'),
        ),
    ]
