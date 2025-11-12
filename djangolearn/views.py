from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello World! HOME")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("Hello World! ABOUT")
    return render(request, 'about.html')

def contact(request):
    return HttpResponse("Hello World! CONTACT")