from django.shortcuts import render
from . import forms, models

# Create your views here.
def homeView(request):
    
    if request.method=='POST':
        form=forms.SearchForm(request.POST)
        country_form=forms.CountrySearchForm(request.POST)
        
    else:
        form=forms.SearchForm()
        country_form=forms.CountrySearchForm()

    return render(request, 'home/home.html', {'form': form, 'countryform': country_form})