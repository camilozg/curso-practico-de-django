from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', views.EmailUpdate.as_view(), name='profile_email'),
]
