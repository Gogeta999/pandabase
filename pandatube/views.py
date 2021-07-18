from django.shortcuts import render
from django.views.generic import FormView, TemplateView
# Create your views here.
class Index(TemplateView):
    template_name = 'main/index.html'
