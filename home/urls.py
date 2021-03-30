from django.urls import path, include 
from .views import homeView, aboutView, howtoView, faqView, contactView

app_name='home'

urlpatterns = [
    path('', homeView, name='home'),
    path('', aboutView, name='about'),
    path('', howtoView, name='howto'),
    path('', faqView, name='faq'),
    path('', contactView, name='contact')
]