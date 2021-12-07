from django.shortcuts import render
from .models import Profile, Contact
# Create your views here.

def index(request):
    profile = Profile.objects.all()
    return render(request, 'index.html', {'profile':profile})

def contactview(request):
    return render(request, 'contact.html')