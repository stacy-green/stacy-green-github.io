from django.db import models
from django.contrib.auth.models import AbstractUser

class Location(models.Model):
    latitude = models.DecimalField(decimal_places=5, max_digits=7)
    longitude = models.DecimalField(decimal_places=5, max_digits=8)
    timezone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"

class Group(models.Model):
    name = models.CharField(max_length=20)
    private = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name="users", blank=True)
    private = models.BooleanField(default=True)
    restricted = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# User
# - username
# - password
# - location (ForeignKey)
# - groups (ManyToMany)
# - private

# Location
# - latitude
# - longitude
# - timezone (nullable)

# Group
# - name
# - private
# - events (default=None)