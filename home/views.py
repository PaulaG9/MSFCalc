from django.shortcuts import render
from . import forms, models

# Create your views here.
def homeView(request):
    
    if request.method=='POST':
        form=forms.SearchForm(request.POST)
    else:
        form=forms.SearchForm()
 
    return render(request, 'home/home.html', {'form': form})