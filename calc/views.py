from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from calc import forms, models
from home.views import homeView
from home.forms import SearchForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from calc.models import Disease, Supply

# Create your views here.
def calculatorView(request):
    if request.method=='POST': 

        # search_form=SearchForm(request.POST)
        search_item=request.POST.get('disease_search')
        
        try:
            queryset=Supply.objects.filter(disease_supply=search_item)
        
        except ObjectDoesNotExist:
            queryset=[]
    
          
        forecast_form=forms.ForecastForm(request.POST)
                  
        return render(request, 'calc/forecast.html', {'forecast_form': forecast_form, 'queryset':queryset,'searchitem':search_item})
    else:
        return render (request, 'calc/forecast.html', )




def resultsView():
    pass
