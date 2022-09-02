from django.db import models

# Create your models here.
class PokemonType(models.Model):
    name = models.CharField(max_length=16)
    
    def __str__(self):
        return f"{self.name}"

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=64)
    height = models.FloatField()
    weight = models.FloatField()
    image_front = models.CharField(max_length=256)
    image_back = models.CharField(max_length=256)
    types = models.ManyToManyField(PokemonType, related_name="types", blank=True)

    def __str__(self):
        type_query = list((self.types.values('name')))
        type_string = ''
        type_list = []
        for query in type_query:
            type_list.append(query.get("name"))
        type_string += ", ".join(type_list)
        return f"No: {self.number}, Name: {self.name}, Types: {(type_string)}"
