from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_view(request):
    return render(request, 'index.html')

def login(request):
   return render(request, 'login.html')

def signup(request):
   return render(request,'signup.html')
