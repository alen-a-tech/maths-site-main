# admin.py

from django.contrib import admin
from .models import Animal, AnimalClass

admin.site.register(Animal)       # Регистрация модели Animal
admin.site.register(AnimalClass)  # Регистрация модели AnimalClass
