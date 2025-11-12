from django.shortcuts import render

# Create your views here.
def all_testapp(request):
    return render(request, 'testapp/all_testapp.html')