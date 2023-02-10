from django import forms
from .models import Page


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = '__all__'
        labels = {
            'title': 'Ingresa un título',
            'content': 'Ingresa el contenido'
        }
        # widgets = {
        #     'title': forms.TextInput(attrs={'class':'form-control','placeholder': 'Título'})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Removes : as label suffix
        self.label_suffix = ""
        # Agrega placeholders
        placeholders = {
            'title': 'Título'
        }
        for field in self.fields:
            if field in placeholders:
                self.fields[field].widget.attrs['placeholder'] = placeholders[field]
        # for field in self.fields:
        #     self.fields[field].widget.attrs['class'] = 'form-control'
