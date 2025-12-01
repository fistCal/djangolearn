from django.shortcuts import render
from .models import testappVariety, Airplane
from django.shortcuts import get_object_or_404
from .forms import testappVarietyForm


# Create your views here.
def all_testapp(request):
    seats = testappVariety.objects.all()
    return render(request, 'testapp/all_testapp.html', {'Seats': seats})

def seat_detail(request, seat_id):
    seat = get_object_or_404(testappVariety, pk=seat_id)
    return render(request, 'testapp/testapp_detail.html', {'seat': seat}) 

def seat_store_view(request):
    stores = None
    if request.method == 'POST':
        form = testappVarietyForm(request.POST)
        if form.is_valid():
            seat_variety = form.cleaned_data['seat_variety']        
            # form name : seat_variety
            stores = Airplane.objects.filter(seat_variety=seat_variety)
    else:
        form = testappVarietyForm()
    return render(request, 'testapp/testapp_store.html', {'stores': stores, 'form': form})