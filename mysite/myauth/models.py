from django.contrib.auth.models import User, Group
from django.db import models

# создать автоматическое добавление ролей (Админ, Покупатель)


def user_directory_path(instance, filename):
    return 'profile_{0}/{1}'.format(instance.user.id, filename)


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = "Профили"

    name = models.CharField(max_length=50, blank=False, verbose_name="Имя")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="Пользователь")
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="Номер телефона")
    address = models.CharField(max_length=255, blank=True, verbose_name="Адрес")
    email = models.EmailField(blank=False, verbose_name="Почта")
    image = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name='Аватар')
    role = models.ForeignKey(Group, on_delete=models.PROTECT,
                             # default=Group.objects.get(name="Покупатель"),
                             blank=True,
                             default=2,
                             related_name='role',
                             verbose_name="Роль"
                             )

    # def save(self, *args, **kwargs):
    #     try:
    #         self.role
    #     except:
    #         self.role = Group.objects.get(name="Покупатель")
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# class UserRole(models.Model):
#     class Meta:
#         ordering = ['role']
#         verbose_name = 'Роль'
#         verbose_name_plural = "Роли"
#
#     # USER_ROLE_CHOICES = [('Admin', 'Администратор'),
#     #                      ('Customer', 'Покупатель'),
#     #                      # ('Unregistered', 'Незарегистрированный пользователь')
#     #                      ]
#
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="role", verbose_name="Пользователь")
#     # role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='Customer', verbose_name="Роль")
#     role = models.ForeignKey(Group, on_delete=models.PROTECT,
#                              # default=Group.objects.get(name="Покупатель"),
#                              blank=True,
#                              related_name='role',
#                              verbose_name="Роль"
#                              )
#
#
#
#     # def get_role_display_name(self):
#     #     for choice in self.USER_ROLE_CHOICES:
#     #         if choice[0] == self.role:
#     #             return choice[1]
#     #     return self.role
#
#
#     def save(self, *args, **kwargs):
#         try:
#             self.role
#         except:
#             self.role = Group.objects.get(name="Покупатель")
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.role
