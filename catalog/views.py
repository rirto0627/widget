from os import getcwd

from django.shortcuts import render
import json
from .models import widget, Menu, Datetime_Picker, Checkbox_Group, Combo_Box, Text_Input
from catalog.models import widget


# Create your views here.
def home(request):
    # style從json更改
    # css = 'second'
    # style = f'/css/{css}.css'
    css1 = '/css/app.c8413253.css'
    css2 = '/css/chunk-vendors.35c65227.css'
    css3 = '/css/chunk-vendors.35c65227.css'
    css4 = '/css/app.c8413253.css'
    js1 = '/js/app.84f32b18.js'
    js2 = '/js/chunk-vendors.c13c749a.js'
    js3 = '/js/chunk-vendors.c13c749a.js'
    js4 = '/js/app.84f32b18.js'
    icon = f"/favicon.ico"
    with open('./templates/home/config.json', 'r', encoding='utf8') as jf:
        jd = json.load(jf)
    return render(request, 'home/index.html',

                  {
                      'json': jd,
                      'css1': css1,
                      'css2': css2,
                      'css3': css3,
                      'css4': css4,
                      'js1': js1,
                      'js2': js2,
                      'js3': js3,
                      'js4': js4,
                      'icon': icon
                  }
                  )


def config(request):
    # front_list = front.objects.all()
    return render(request, 'home/config.json', )
