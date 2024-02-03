from django import forms
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from .models import Author


# Create your views here.
class AuthorPageView(DetailView):
    template_name = 'authors/author-details.html'
    model = Author
    context_object_name = 'author'


class CreateAuthorView(CreateView):
    model = Author
    fields = ['fullname', 'born_date', 'born_location', 'description']
    template_name = 'authors/author-create-form.html'

    def get_form(self, form_class=None):
        form = super(CreateAuthorView, self).get_form(form_class)
        form.fields['born_date'].widget = forms.DateInput(attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                })
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(to='authors:create.author')
