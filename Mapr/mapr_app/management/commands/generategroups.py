from django.core.management.base import BaseCommand
import random
from mapr_app.models import Group, User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.all()
        Group.objects.all().delete()
        groups = []
        for x in range(3):
            group = Group()
            group.name = f"Test Group {x}"
            group.save()
            groups.append(group)

        for user in users:
            group = random.choice(groups)
            user.groups.add(group)
            user.save()



