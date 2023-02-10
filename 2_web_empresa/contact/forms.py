from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True)
    email = forms.EmailField(label='Email', required=True)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix
