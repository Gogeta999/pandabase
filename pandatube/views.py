from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import FormView, TemplateView
from .models import Video, User
from django.urls import reverse_lazy
from .forms import  UserRegisterForm

# Create your views here.
class Index(TemplateView):
    template_name = 'main/index.html'

#Use Login From auth.accounts
# class UserLoginPage(TemplateView):
#     form_class = UserLoginForm
#     template_name = 'registration/login.html'

class UserRegisterPage(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')


