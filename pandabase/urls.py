from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='pandabase/', permanent=False), name='index'),
    path('secret/admin', admin.site.urls, name='admin'),
    path(r'pandabase/', include("pandatube.urls")),
    path('accounts/', include('django.contrib.auth.urls'))
]

# Use static() to add url mapping to serve static files during development (only)



