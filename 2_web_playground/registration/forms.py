from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # valida si el email ya está registrado para alguno de los usuarios
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya está registrado')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removes : as label suffix
        self.label_suffix = ""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Biografía'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Enlace'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removes : as label suffix
        self.label_suffix = ""
        # Agrega placeholders
        # placeholders = {
        #     'title': 'Título'
        # }
        # for field in self.fields:
        #     if field in placeholders:
        #         self.fields[field].widget.attrs['placeholder'] = placeholders[field]


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ['email']

    # Valida si el email modificado ya está registrado para alguno de los usuarios
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya está registrado')
        return email
