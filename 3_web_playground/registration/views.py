from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django import forms
from django.shortcuts import render, redirect

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self):
        form = super().get_form()
        form.label_suffix = ""  # Removes : as label suffix
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Email',
            'password1': 'Contraseña',
            'password2': 'Contraseña (confirmación)'
        }
        placeholders = {
            'username': 'Nombre de usuario',
            'email': 'Dirección email',
            'password1': 'Contraseña',
            'password2': 'Repite la contraseña'
        }
        for field in form.fields:
            form.fields[field].widget.attrs['class'] = 'form-control mb-2'
            if field in placeholders:
                form.fields[field].widget.attrs['placeholder'] = placeholders[field]
            if field in labels:
                form.fields[field].label = labels[field]
        return form


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    # fields = ['avatar', 'bio', 'link']
    form_class = ProfileForm
    template_name = 'registration/profile_form.html'
    success_url = reverse_lazy('registration:profile')

    def get_object(self):
        # recuperamos el objeto que se va a editar
        # si el perfil no existe entonces lo crea
        (profile, created) = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            profile = self.get_object()

            # if request.FILES.get('avatar', False):
            #     profile.avatar = request.FILES['avatar']

            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']

            if 'avatar-clear' in request.POST:
                profile.avatar.delete()

            profile.bio = request.POST['bio']
            profile.link = request.POST['link']
            profile.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})


class EmailUpdate(LoginRequiredMixin, UpdateView):
    # model = Profile
    # fields = ['avatar', 'bio', 'link']
    form_class = EmailForm
    template_name = 'registration/profile_email_form.html'
    success_url = reverse_lazy('registration:profile')

    def get_object(self):
        return self.request.user

    def get_form(self):
        form = super().get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form
