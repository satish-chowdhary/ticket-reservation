from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        field = ['Name', 'Gender', 'Age', 'select_coach']

