from django.shortcuts import render
import random
import requests
from bs4 import BeautifulSoup

# Create your views here.
def poke_members(request, username):
    poke_num = [str(i).zfill(4) for i in range(1, 1026)]
    my_pokemon_numbers = random.choice(poke_num)

    context = {
        'username': username,
        'my_pokemon_numbers': f'https://data1.pokemonkorea.co.kr/newdata/pokedex/full/{my_pokemon_numbers}01.png'
,
    }

    # Django 템플릿에 데이터 전달
    return render(request, 'poke_members.html', context)