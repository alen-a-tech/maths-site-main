from rest_framework import serializers
from .models import AnimalClass, Animal

class AnimalClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalClass
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
