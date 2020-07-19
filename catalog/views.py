from django.shortcuts import render
import json
from .models import front
from catalog.models import widget
with open('setting.json', 'r', encoding='utf8') as jfile:
    jd = json.load(jfile)

# Create your views here.
def home(request):
    # style從json更改
    css = 'second'
    style = f'/css/{css}.css'
    for menu in jd['menu']:
        menu_id = menu['id']
        menu_align = menu['align']


    menu_items_id = jd['menu'][0]['items'][0]['id']
    return render(request, 'home/home.html', {'style': style, })


def front(request):
    # front_list = front.objects.all()
    return render(request, 'home/index.html',)
