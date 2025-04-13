from django.core.exceptions import ValidationError
from django.db import models

class AnimalClass(models.Model):
    name = models.CharField(max_length=100, verbose_name="Animal Class")
    description = models.TextField(blank=True)

    def clean(self):
        if not self.name:
            raise ValidationError("Название класса животного обязательно.")
        if len(self.name) < 3:
            raise ValidationError("Название класса должно быть не менее 3 символов.")

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    animal_class = models.ForeignKey(AnimalClass, on_delete=models.CASCADE)

    def clean(self):
        if not self.name:
            raise ValidationError("Название животного обязательно.")
        if len(self.name) < 3:
            raise ValidationError("Название животного должно быть не менее 3 символов.")

    def __str__(self):
        return self.name
