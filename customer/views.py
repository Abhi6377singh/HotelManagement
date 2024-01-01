from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse

# Create your views here.


def index_view(request):
    return render(request, 'index.html')
>>>>>>> bfe8b4c80a479c020f9c7ee3912fe8dfddd817a5
