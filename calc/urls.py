from django.urls import path, include 
from .views import *

app_name='calc'

urlpatterns = [
   path('forecast/', calculatorView, name='forecast'),
   path('results/', resultsView, name='results'),
   path('export/', tableExport, name='export'),
   
]