# Generated by Django 4.1.7 on 2023-04-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypayment', '0002_alter_payment_order_alter_payment_payment_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='summary_price',
            field=models.DecimalField(decimal_places=2, default='999.99', max_digits=7, verbose_name='Общая стоимость'),
        ),
    ]
