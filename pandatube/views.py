from django.shortcuts import render
from django.template import context_processors
from django.views.generic import FormView, TemplateView
from .models import Video

# Create your views here.
class Index(TemplateView):
    template_name = 'main/index.html'


