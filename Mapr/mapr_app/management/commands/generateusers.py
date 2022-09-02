from django.core.management.base import BaseCommand

from mapr_app.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.filter(is_staff=False).delete()
        for x in range(0, 10):
            user = User.objects.create_user(f"testUser{x}", "", "password")
            if x%2:
                user.private = False
            else:
                user.private = True
            user.save()
            print(f"Created user testUser{x}")
        
