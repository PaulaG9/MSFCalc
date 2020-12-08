from django import forms
from django.forms import ModelForm
from django_select2 import forms as s2forms
from calc.models import Supply, Disease

class SearchForm(forms.Form):
    disease_search=forms.ModelMultipleChoiceField(required=False,
        queryset=Disease.objects.all(),
        label='',
        widget=s2forms.ModelSelect2MultipleWidget(
            model=Disease,
            search_fields=['disease_name__icontains'],
            # dependent_fields={'pharmacy_search':'pharmacy_searches'}
        )
    )
   
    # pharmacy_search = forms.ModelMultipleChoiceField(required=False,
    #     queryset=Supply.objects.all(),
    #     label='',
    #     widget=s2forms.ModelSelect2MultipleWidget(
    #         model=Pharmacy,
    #         search_fields=['msf_code__icontains','medicine_name__icontains', 'disease_medicine__disease_name__icontains'],
    #         dependent_fields={'disease_search':'disease_searches'}
    #     )
    # )

