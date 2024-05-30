from django.contrib import admin

from .models import Cate_Service, Service

# Register your models here.
@admin.register(Service)
class AdminService(admin.ModelAdmin):
    ...


@admin.register(Cate_Service)
class AdminCate_Service(admin.ModelAdmin):
    ...