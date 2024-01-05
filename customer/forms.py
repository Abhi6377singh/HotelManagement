# forms.py
from django import forms

class BookingForm(forms.Form):
    checkin_date = forms.DateField(label='Check-in Date',widget=forms.DateInput(attrs={'type': 'date'}))
    checkout_date = forms.DateField(label='Checkout Date',widget=forms.DateInput(attrs={'type': 'date'}))
