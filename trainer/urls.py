# trainer/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnimalClassViewSet, AnimalViewSet

router = DefaultRouter()
router.register(r'animal_classes', AnimalClassViewSet)
router.register(r'animals', AnimalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
