from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_view(request):
    return render(request, 'index.html')

def login(request):
   return render(request, 'login.html')

def signup(request):
   return render(request,'signup.html')

def about_view(request):
   return render(request,'about.html')

def service_view(request):
   return render(request,'services.html')

def contact_view(request):
   return render(request,'contact.html')