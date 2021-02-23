from django import forms
from django.forms import ModelForm
from django_select2 import forms as s2forms
from calc.models import Supply, Disease
from home.forms import SearchForm
from django.db.models import Q
from django.shortcuts import render

class ForecastForm(forms.Form):
    num_patients=forms.IntegerField(label='Patients/drug', help_text='What is the number of patients you expect to have at the start of the programme?')
    duration=forms.ChoiceField(label='Duration in days', choices=[('1', '1 month'), ('2', '2 months'), ('3', '3 months'), ('6', '6 months')])
    monthly_increase=forms.IntegerField(label='Monthly increase', help_text='What increase do you expect to see in the number of patients. Please express the numbers in patient numbers')
    frequency=forms.ChoiceField(label="Frequency of intake", choices=Supply.supply_frequency.field.get_choices(include_blank=False))
    unit_per_patient=forms.IntegerField(label="Units/patient", help_text="How many units do the patients take on average?")
    patients_in_cohort=forms.IntegerField(label="Total patients in cohort")
    

# class SupplyForm(forms.ModelForm):
#     def getSearchField(self, request):
#         search_form=SearchForm(self.request.POST)
#         if search_form.is_valid():
#             search_item=search_form.cleaned_data
#         return search_item

#     class Meta:
#         model=Supply
#         fields=['frequency']
    
#         def __init__(self, *args, **kwargs):
#             super(SupplyForm, self).__init__(*args, **kwargs)
#             self.fields['msf_code'].widget.attrs['readonly']=True
#             self.fields['medicine_name'].widget.attrs['readonly']=True
#             self.fields['msf_code'].queryset=Supply.objects.filter(Q(disease_medicine__disease_name__icontains=self.getSearchForm()))
#             self.fields['medicine_name'].queryset=Supply.objects.filter(Q(disease_medicine__disease_name__icontains=self.getSearchForm()))

              