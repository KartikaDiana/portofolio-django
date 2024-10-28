from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'myApp/home.html')

def profile(request):
    return render(request, 'myApp/profile.html')

def education(request):
    return render(request, 'myApp/education.html')

def organization(request):   
    return render(request, 'myApp/organization.html')

def contact(request):   
    return render(request, 'myApp/contact.html')