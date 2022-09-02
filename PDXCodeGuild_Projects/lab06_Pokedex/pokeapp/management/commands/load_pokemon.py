from django.core.management.base import BaseCommand
from pokeapp.models import Pokemon, PokemonType
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        f = open("pokeapp\management\commands\pokemon.json")
        contents = json.load(f)
        all_types = []
        for x in range(len(contents['pokemon'])):
        # for x in range(5): # for testing purposes
            #### add pokemon first, before manytomany
            poke = Pokemon()
            poke.number = contents["pokemon"][x]["number"]
            poke.name = contents['pokemon'][x]['name']
            poke.height = contents["pokemon"][x]["height"] / 10
            poke.weight = contents["pokemon"][x]["weight"] / 10
            if contents["pokemon"][x]["image_front"] == None:
                poke.image_front = "No front image available"
            else:
                poke.image_front = contents["pokemon"][x]["image_front"]
            if contents["pokemon"][x]["image_back"] == None:
                poke.image_back = "No back image available"
            else:
                poke.image_back = contents["pokemon"][x]["image_back"]
            poke.save() #### have to save, Pokemon object has to exist and be saved before manytomany relationship can be established

            #### create pokemontypes
            pokemon_types = contents["pokemon"][x]["types"]
            for single_type in pokemon_types:
                if single_type not in all_types:
                    all_types.append(single_type)
                    new_type = PokemonType()
                    new_type.name = single_type
                    new_type.save()

            #### create manytomany relationship
            for type in pokemon_types:
                newtype = PokemonType.objects.get(name=type)
                poke.types.add(newtype)
            
            poke.save() #### final save after manytomany relationship is established


