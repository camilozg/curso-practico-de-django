from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about-me', views.about, name='about'),
    path('contacto', views.contact, name='contact')
]
