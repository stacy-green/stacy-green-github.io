from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon, PokemonType
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        PokemonType.objects.all().delete()
        f = open("pokeapp\management\commands\pokemonTypes.json")
        contents = json.load(f)
        for x in range(len(contents['types'])):
            type = PokemonType()
            type.name = contents["types"][x]
            type.save()
            print(type.name)
        
