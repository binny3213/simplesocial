from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from . import forms

# Create your views here.
class TestPage(TemplateView):
    template_name = 'test.html'
    
class ThanksPage(TemplateView):
    template_name = 'thanks.html'    

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'