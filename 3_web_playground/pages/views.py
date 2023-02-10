from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PageListView(ListView):
    # template_name = page_list.html
    # context_object_name = page_list
    # queryset = Page.objects.all()
    model = Page


class PageDetailView(DetailView):
    # template_name = page_detail.html
    # context_object_name = page
    model = Page


class PageCreateView(LoginRequiredMixin, CreateView):
    # template_name = page_form.html
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    login_url = reverse_lazy('admin:login')

    # en lugar de usar un ModelForm, podemos sobreescribir el metodo get_form() para
    # definir los labels, placeholders y eliminar el label_suffix
    # def get_form(self):
    #     form = super().get_form()
    #     form.label_suffix = ""  # Removes : as label suffix
    #     labels = {
    #         'title': 'Título (mod)',
    #         'content': 'Contenido (mod)'
    #     }
    #     placeholders = {
    #         'title': 'Título',
    #     }
    #     for field in form.fields:
    #         if field in labels:
    #             form.fields[field].label = labels[field]
    #         if field in placeholders:
    #             form.fields[field].widget.attrs['placeholder'] = placeholders[field]
    #     return form


class PageUpdateView(LoginRequiredMixin, UpdateView):
    # template_name = page_form.html (default)
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    # se puede sobreescribir el metodo get_success_url para poder concatenar parámetros en la url
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDeleteView(LoginRequiredMixin, DeleteView):
    # template_name = page_confirm_delete.html
    model = Page
    success_url = reverse_lazy('pages:pages')
