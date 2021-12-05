from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
admin.site.register(Profile, ProfileAdmin)