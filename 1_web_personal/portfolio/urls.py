from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('portafolio', views.portfolio, name='portfolio')
]
