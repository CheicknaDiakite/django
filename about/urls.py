from django.urls import path

from .views import about, about_category

urlpatterns = [
    path('', about, name='about'),
    path('categorie/<str:slug>', about_category, name='about_category'),
]