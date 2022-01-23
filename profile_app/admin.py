from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Profile, Contact
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'profile_pic']
admin.site.register(Profile, ProfileAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
admin.site.register(Contact, ContactAdmin)