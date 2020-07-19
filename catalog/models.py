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

class front(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
