from django.urls import path

from .views import service, service_category

urlpatterns = [
    path('', service, name='service'),
    path('categorie/<str:slug>', service_category, name='service_category'),
]