from django.shortcuts import render
import random
import requests
from bs4 import BeautifulSoup

# Create your views here.
def poke_members(request, username):
    poke_num = [str(i).zfill(4) for i in range(1, 1026)]
    my_pokemon_numbers = random.sample(poke_num, 6)
    for my_pokemon_num in my_pokemon_numbers:
        my_pokemon_num = my_pokemon_num

    context = {
        'username': username,
        'my_pokemon_numbers': my_pokemon_numbers
    }
       

    # Django 템플릿에 데이터 전달
    return render(request, 'poke_members.html', context)