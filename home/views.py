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

def aboutView(request):
    return render(request, 'home/about.html')

def howtoView(request):
    return render(request, 'home/howto.html')

def faqView(request):
    return render(request, 'home/faq.html')

def contactView(request):
    return render(request, 'home/contact.html')

