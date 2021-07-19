from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path('', RedirectView.as_view(url='pandabase/', permanent=False), name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path(r'pandabase/', include("pandatube.urls")),
    path('accounts/', include('django.contrib.auth.urls'))
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



