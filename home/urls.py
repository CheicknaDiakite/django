from django.urls import path

from .views import home


urlpatterns = [
    path('', home, name='home' ),
    # path('', root_index, name='roout_index'),
]