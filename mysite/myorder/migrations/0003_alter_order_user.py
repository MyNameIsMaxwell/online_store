# Generated by Django 4.1.7 on 2023-04-17 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0005_alter_userprofile_role'),
        ('myorder', '0002_alter_order_status_alter_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='myauth.userprofile', verbose_name='Пользователь'),
        ),
    ]
