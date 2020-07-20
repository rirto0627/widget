from django.db import models
from django import forms

from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

import uuid  # Required for unique book instances


# Create your models here.

class widget(models.Model):
    user = models.CharField(max_length=20)
    sex_type_choice = [
        (0, '男'),
        (1, '女'),
    ]
    Sex = models.CharField(default=0,
                           max_length=2,
                           choices=sex_type_choice, )
    language_type_choice = [
        (0, '繁體中文'),
        (1, '英文'),
    ]
    Language = models.CharField(default=0,
                                max_length=2,
                                choices=language_type_choice, )


class Menu(models.Model):
    menu = models.CharField(max_length=20)


class Datetime_Picker(models.Model):
    datetime_picker = models.DateField(default=['%d/%m/%Y'],
                                       )


class Checkbox_Group(models.Model):
    sex_type_choice = [
        (0, '男'),
        (1, '女'),
    ]
    Sex = models.CharField(default=0,
                           max_length=2,
                           choices=sex_type_choice, )


class Combo_Box(models.Model):
    language_type_choice = [
        (0, '繁體中文'),
        (1, '英文'),
    ]
    language = models.CharField(default=0,
                                max_length=2,
                                choices=language_type_choice, )


class Text_Input(models.Model):
    member_id = models.CharField(max_length=20)
    keyword = models.CharField(max_length=20)
