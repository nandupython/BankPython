

from django import forms
from .models import District, Branch

class ApplicationForm(forms.Form):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    ACCOUNT_TYPE_CHOICES = [('-------','-------'),('savings', 'Savings Account'), ('current', 'Current Account')]
    MATERIAL_CHOICES = [('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')]

    name = forms.CharField(max_length=100)
    dob = forms.DateField( widget=forms.DateInput(attrs={'type': 'date'}),)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    phone_number = forms.CharField(max_length=15)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    district = forms.ModelChoiceField(queryset=District.objects.all())
    branch = forms.ModelChoiceField(queryset=Branch.objects.none())  # We will populate this using JavaScript on the frontend.
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES)
    materials_provided = forms.MultipleChoiceField(choices=MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple)

