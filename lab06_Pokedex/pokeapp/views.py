from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pokemon
import json

# Create your views here.
def index(request):

    return render(request, "pokeapp/index.html")

# def pokemon(request):
#     if request.method == "GET":
#         search_term = request.GET.get("searchTerm")
#         if search_term != None:
#             pokemon = Pokemon.objects.filter(name__contains=f"{search_term}")
#             data = list(pokemon.values("number", "name", "image_front"))
#             return JsonResponse({"data": data}, safe=False)
#         else:
#             pokemon = Pokemon.objects.all()
#             data = list(pokemon.values("number", "name", "image_front"))
#             return JsonResponse({"data": data}, safe=False)
   
def pokemon(request):
        search_term = request.GET.get("searchTerm")
        if search_term != None:
            pokemon = Pokemon.objects.filter(name__contains=f"{search_term}")
            data_to_return = pokemon.values("number", "name", "image_front")
            paginator = Paginator(data_to_return, 20)
            page_number = request.GET.get('page')
            data = list(paginator.get_page(page_number))
            return JsonResponse({"data": data}, safe=False)
        else:
            pokemon = Pokemon.objects.all()
            data_to_return = pokemon.values("number", "name", "image_front")
            paginator = Paginator(data_to_return, 20)
            page_number = request.GET.get('page')
            print(paginator.num_pages)
            data = list(paginator.get_page(page_number))
            data.append(paginator.num_pages)
            return JsonResponse({"data": data}, safe=False)