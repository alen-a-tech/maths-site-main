# trainer/views.py
from rest_framework import viewsets
from .models import AnimalClass, Animal
from .serializers import AnimalClassSerializer, AnimalSerializer

class AnimalClassViewSet(viewsets.ModelViewSet):
    queryset = AnimalClass.objects.all()
    serializer_class = AnimalClassSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

# в trainer/views.py
from django.shortcuts import render
from .models import Animal

def animal_list_view(request):
    animals = Animal.objects.all()
    return render(request, 'trainer/animal_list.html', {'animals': animals})
