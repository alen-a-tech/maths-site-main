# proj_maths/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('trainer.urls')),  # ⬅️ Переместили выше
    path('', views.index, name='home'),
    path('animals/', views.AnimalListView.as_view(), name='animals-list'),  # 🦁
    path('add-term/', views.add_term, name='add-animal'),        # ➕
    path('send-term/', views.send_term, name='send-term'),       # 📤
    path('stats/', views.show_stats, name='statistics'),         # 📊
    path('admin/', admin.site.urls),
]
