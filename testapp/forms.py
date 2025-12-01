from django import forms
from .models import testappVariety


class testappVarietyForm(forms.Form):
    seat_variety = forms.ModelChoiceField(
        queryset=testappVariety.objects.all(), 
        label='Select Seat',
        widget=forms.Select(attrs={
            'class': 'px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
            })
    )