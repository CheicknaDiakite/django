from django.contrib import admin

from .models import About, Cate_About

# Register your models here.
@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    ...


@admin.register(Cate_About)
class AdminCate_About(admin.ModelAdmin):
    ...