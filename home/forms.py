from django import forms
from django.forms import ModelForm
from django_select2 import forms as s2forms
from calc.models import Supply, Disease
from home.models import Country

class SearchForm(forms.Form):
    # disease_search=forms.ModelMultipleChoiceField(required=False, -- use the multiple version of this form when wanting to activate multiple NCD selection
    disease_search=forms.ModelChoiceField(help_text="Note: at the moment only diabetes is available in the system. Other NCDs will be added later", required=False,
        queryset=Disease.objects.all().order_by('disease_name'),
        label='Condition/NCD',
        # widget=s2forms.ModelSelect2MultipleWidget( -- use the multiple version of this widget when wanting to activate multiple NCD selection
         widget=s2forms.ModelSelect2Widget(   
            model=Disease,
            search_fields=['disease_name__icontains'],
            # dependent_fields={'pharmacy_search':'pharmacy_searches'}
        )
    )
   
class CountrySearchForm(forms.Form):
    country_search=forms.ModelChoiceField(help_text="This should be your host country or the country where your target population comes from", required=False,
            queryset=Country.objects.all().order_by('country_name'),
            label='Target Country',
            widget=s2forms.ModelSelect2Widget(
                model=Country,
                search_fields=['country_name__icontains'],
            )
        )

