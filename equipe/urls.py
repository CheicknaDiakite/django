from django.urls import path

from .views import equipe

urlpatterns = [
    path('', equipe, name='equipe')
]