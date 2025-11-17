from django.shortcuts import render
from .models import testappVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_testapp(request):
    seats = testappVariety.objects.all()
    return render(request, 'testapp/all_testapp.html', {'Seats': seats})

def seat_detail(request, seat_id):
    seat = get_object_or_404(testappVariety, pk=seat_id)
    return render(request, 'testapp/testapp_detail.html', {'seat': seat}) 