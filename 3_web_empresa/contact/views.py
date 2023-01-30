from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.


def contact(request):
    contact_form = ContactForm()
    context = {'form': contact_form}

    if request.method == 'POST':
        filled_form = ContactForm(request.POST)
        if filled_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            email_message = EmailMessage(
                'La Cafettira: Nuevo mensaje de contacto',  # asunto
                f'De {name} <{email}>\n\nEscribió:\n\n{content}',  # cuerpo
                'no-contestar@inbox.mailtrap.io',  # email_origen
                [email],  # email_destino
            )
            try:
                email_message.send()
                return redirect(reverse('contact:contact') + '?ok')
            except:
                return redirect(reverse('contact:contact') + '?fail')

    return render(request, 'contact/contact.html', context)
