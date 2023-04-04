from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from django.utils import timezone


class Command(BaseCommand):
    pass
    # help = 'Displays current time'
    #
    # def handle(self, *args, **kwargs):
    #     time = timezone.now().strftime('%X')
    #     self.stdout.write("It's now %s" % time)

# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         self.stdout.write("Create order")
#         user = User.objects.get(username="admin")
#         order = Order.objects.get_or_create(
#             delivery_address="Minskaya st., 8",
#             promocode="SALE133",
#             user=user,
#         )
#         self.stdout.write(f"Created order {order}")
