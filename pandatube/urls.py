from django.urls import path
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path(r'signup/', views.UserRegisterPage.as_view(), name='signup'),
]