from django.shortcuts import render
from django.http import HttpResponse #use for front end
# Create your views here.
def home(request):
    return HttpResponse("This is my Django Project")

