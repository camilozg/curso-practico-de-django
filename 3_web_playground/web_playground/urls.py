"""web_playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('pages/', include('pages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profiles/', include('profiles.urls')),
    path('messenger/', include('messenger.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ----------------------------------------------------------------
# El include django.contrib.auth.urls agrega las siguientes rutas
# ----------------------------------------------------------------
# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']
# ----------------------------------------------------------------------------------------------
# Para sobreescribir las templates de autenticación por defecto hay que crearlas con los estos nombres
# Podemos tomar como base los templates por defecto del repositorio de django y modificarlos
# https://github.com/django/django/tree/main/django/contrib/admin/templates/registration
# Los templates de login.html y signup.html no existen por defecto, siempre debemos crearlos
# ----------------------------------------------------------------------------------------------
# logged_out.html
# password_change_done.html
# password_change_form.html
# password_reset_complete.html
# password_reset_confirm.html
# password_reset_done.html
# password_reset_email.html
# password_reset_form.html
