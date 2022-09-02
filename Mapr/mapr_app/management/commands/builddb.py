from django.core.management.base import BaseCommand
import random
from mapr_app.models import Group, User, Location

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.filter(username__icontains="testUser").delete()
        Location.objects.filter(user__username__isnull=True).delete()
        Group.objects.filter(name__icontains="test").delete()

        groups = []
        for x in range(5):
            group = Group()
            group.name = f"TestGroup{x}"
            group.private = False
            group.save()
            groups.append(group)

        for x in range(20):
            user = User.objects.create_user(f"testUser{x}", "", "password")
            if x % 2:
                user.private = False
            if x %5 == 0:
                user.restricted = True
            groups_to_add = random.choices(groups, k=random.randint(1, 3))
            for group in groups_to_add:
                user.groups.add(group)
    
            if user.location:
                continue
            location = Location()
            latitude = round(random.randrange(-9000000, 9000000) / 100000, 5)
            longitude = round(random.randrange(-18000000, 18000000) / 100000, 5)

            location.latitude = latitude
            location.longitude = longitude
            location.save()

            user.location = location
            user.save()
            print(f"Created user testUser{x}, private: {user.private}, restricted: {user.restricted}")


        # for user in users:
        #     group = random.choice(groups)
        #     user.groups.add(group)
        #     user.save()
