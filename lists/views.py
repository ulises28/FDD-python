#from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse

def home_page(request):
    return render(request, 'home.html')
    #return HttpResponse("Hello, world. You're at the lists index.")

#def index(request):
#    return HttpResponse("Hello, world. You're at the lists index.")