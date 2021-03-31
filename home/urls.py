from django.urls import path, include 
from .views import homeView, aboutView, howtoView, faqView, contactView

app_name='home'

urlpatterns = [
    path('', homeView, name='home'),
    path('about/', aboutView, name='about'),
    path('howto/', howtoView, name='howto'),
    path('faq/', faqView, name='faq'),
    path('contact/', contactView, name='contact')
]