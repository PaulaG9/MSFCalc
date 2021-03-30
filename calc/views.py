from django.shortcuts import render, redirect
from django_pandas.io import read_frame
from . import forms
from home.views import homeView
from home.forms import SearchForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from calc.models import Disease, Supply, TreatmentLine
from calc.functions import getNetPatients, getEstimate
import numpy as np
import pandas as pd
import json

# Create your views here.
def calculatorView(request):
        
    if request.method=='POST': 
        
        search_form=SearchForm(request.POST)
        if search_form.is_valid():
            search_item=search_form.cleaned_data['disease_search']
        # search_item=request.POST.get('disease_search')
        
        try:           
            queryset=TreatmentLine.objects.filter(tline_disease__in=[search_item]).order_by('tline_id')        
            supply_qset=list(Supply.objects.all().order_by('msf_code'))
        except ObjectDoesNotExist:
            queryset=[]
              
        forecast_form=forms.ForecastForm()
                  
        return render(request, 'calc/forecast.html', {'forecast_form': forecast_form, 'queryset':queryset,'supplyqset':supply_qset})
    else:
        return render (request, 'calc/forecast.html', )


def resultsView(request): 
    global df3   
    if request.method=='POST':
        other_context={}
        context={}
        for k, v in request.POST.items():
            other_context[k]=v
                   
        supply=[]
        for key in other_context.keys():
           if "frequency" in key:
               supply.append(key.split("_")[len(key.split('_'))-1])             
        
        unique_drugs=np.unique(np.array(supply))
        supply_list=Supply.objects.filter(msf_code__in=unique_drugs).order_by('supply_name')     
      
        supply_est={}
        for item in supply_list:        
            tlines=[]
            estimate=0
            fmc=0
            for key in other_context.keys():                
                if item.msf_code in key:
                   tlines.append(key.split('_')[len(key.split('_'))-2])
            
            try:
                for i in range(len(tlines)):
                    numpatients=float(other_context['num_patients_'+str(tlines[i])+'_'+item.msf_code])
                    duration=int(other_context['duration_'+str(tlines[i])])*30 
                    monincrease=int(other_context['monthly_increase_'+str(tlines[i])])
                    # attrrate=int(other_context['attrition_rate_'+str(tlines[i])])
                    frequency=int(other_context['frequency_'+str(tlines[i])+'_'+item.msf_code])
                    #print(numpatients, duration, monincrease,frequency)
                    units=float(other_context['unit_per_patient_'+str(tlines[i])+'_'+item.msf_code])
                    packaging=item.get_packaging_presentation_display()
                    if item.packaging_size:
                        packaging_size=int(item.packaging_size.split(' ')[0])
                    else:
                        pass
                   
                    estimate=getEstimate(getNetPatients(numpatients, duration, monincrease),duration, frequency, units, packaging, packaging_size) 
                    fmc=estimate/(duration/30)

            except ValueError as e:
                print (e)
                next

            supply_est[item.msf_code]=[estimate,fmc]  
       

        df1 = read_frame(supply_list, fieldnames=['msf_code', 'supply_name', 'packaging_presentation']) 
        df1.set_index('msf_code', inplace=True)
        df2=pd.DataFrame.from_dict(supply_est, columns=['estimated_needs', 'fmc'], orient='index')
        #df2=pd.DataFrame(list(supply_est.items()), columns=['msf_code', 'estimated_needs'])
        df3=df1.join(df2)
        print(df1, df2, df3)

       
        json_records = df3.reset_index().to_json(orient ='records') 
        data = [] 
        data = json.loads(json_records)         
        context ['d']=data    

        request.session['dt']=data

        return render(request, 'calc/results.html', context) 

def tableExport(request):
    from django.http import HttpResponse
        
    df=pd.DataFrame(request.session['dt'])
    
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Diabetes Order.xlsx"'

    df.to_excel(response,index=False)
    return response



        
