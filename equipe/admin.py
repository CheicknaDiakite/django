from django.contrib import admin

from .models import Equipe

# Register your models here.
@admin.register(Equipe)
class AdminEquipe(admin.ModelAdmin):
    ...