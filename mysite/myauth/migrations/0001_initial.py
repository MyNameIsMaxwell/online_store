# Generated by Django 4.1.7 on 2023-04-07 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import myauth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('image', models.ImageField(blank=True, upload_to=myauth.models.user_directory_path, verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Admin', 'Администратор'), ('Customer', 'Покупатель')], default='Customer', max_length=20, verbose_name='Роль')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myauth.userprofile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
                'ordering': ['-role'],
            },
        ),
    ]
