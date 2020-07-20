from os import getcwd

from django.shortcuts import render
import json
from .models import widget, Menu, Datetime_Picker, Checkbox_Group, Combo_Box, Text_Input
from catalog.models import widget


# Create your views here.
def home(request):
    # style從json更改
    css = 'second'
    style = f'/css/{css}.css'
    with open('./templates/setting.json', 'r', encoding='utf8') as jf:
        jd = json.load(jf)
    return render(request, 'home/home.html', {'style': style, 'json': jd})


def front(request):
    # front_list = front.objects.all()
    return render(request, 'home/index.html', )
