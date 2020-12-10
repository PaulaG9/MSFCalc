from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from calc import forms, models
from home.views import homeView
from home.forms import SearchForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from calc.models import Disease, Supply, TreatmentLine
import numpy as np

# Create your views here.
def calculatorView(request):
    
    if request.method=='POST': 
        
        search_form=SearchForm(request.POST)
        if search_form.is_valid():
            search_item=search_form.cleaned_data['disease_search']
        #search_item=request.POST.get('disease_search')
        
        try:           
            queryset=TreatmentLine.objects.filter(tline_disease__in=search_item)        
            supply_qset=Supply.objects.all()
        except ObjectDoesNotExist:
            queryset=[]
              
        forecast_form=forms.ForecastForm()
                  
        return render(request, 'calc/forecast.html', {'forecast_form': forecast_form, 'queryset':queryset,'supplyqset':supply_qset})
    else:
        return render (request, 'calc/forecast.html', )


def resultsView(request):    
    if request.method=='POST':
        context={}

        for k, v in request.POST.items():
            context[k]=v
                   
        supply=[]
        for key in context.keys():
           if "frequency" in key:
               supply.append(key.split("_")[len(key.split('_'))-1])             
        
        unique_drugs=np.unique(np.array(supply))
        supply_list=Supply.objects.filter(msf_code__in=unique_drugs)

        def getNetPatients(numpatients, duration, monincrease, attrrate):
            if duration/30>1:
                final_mth_patients=numpatients+(round(duration/30)-1)*(monincrease-attrrate)
                net_patients=((numpatients+final_mth_patients)*round(duration/30))/2
            else:
                net_patients=numpatients+(monincrease-attrrate)
            
            return net_patients
        
        def getEstimate(net_patients, duration, frequency):

            estimate=net_patients * duration * frequency

            return estimate

        supply_est={}
        for item in supply_list:        
            tlines=[]
            estimate=0
            print(item)
            for key in context.keys():
                print(key)
                if item.msf_code in key:
                   tlines.append(key.split('_')[len(key.split('_'))-2])
            print(tlines)
            for i in range(len(tlines)):
                numpatients=int(context['num_patients_'+str(tlines[i])])
                print(type(numpatients), numpatients)
                duration=int(context['duration_'+str(tlines[i])])
                print(type(duration), duration)
                monincrease=int(context['monthly_increase_'+str(tlines[i])])
                print(type(monincrease), monincrease)
                attrrate=int(context['attrition_rate_'+str(tlines[i])])
                print(type(attrrate),attrrate)
                frequency=int(context['frequency_'+str(tlines[i])+'_'+item.msf_code])
                print(type(frequency), frequency)
                estimate=estimate + getEstimate(getNetPatients(numpatients, duration, monincrease, attrrate),duration, frequency)  
            supply_est[item]=estimate

        print(supply_list)
        print(supply_est)
        
        #context['num_patients']=num_patients
        # context['frequency']=frequency
    
        return render(request, 'calc/results.html', {'supply_list':supply_list, 'supply_est':supply_est})
