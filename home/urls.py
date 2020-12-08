from django.urls import path, include 
from .views import homeView

app_name='home'

urlpatterns = [
    path('', homeView, name='home'),
]