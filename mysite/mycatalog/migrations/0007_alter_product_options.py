# Generated by Django 4.1.7 on 2023-04-17 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycatalog', '0006_productcategory_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
