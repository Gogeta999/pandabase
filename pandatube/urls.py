from django.urls import path
from django.views.generic.base import TemplateView
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path(r'signup/', views.UserRegisterPage.as_view(), name='signup'),
    path(r'profile/<int:pk>/', views.UserProfilePage.as_view(), name='profile'),
    path(r'courses/<int:pk>/', views.CoursesPage.as_view(), name='courses'),
    path(r'courses/video/<int:pk>/', views.CourseVideoPage.as_view(), name='video'),
    path('search', views.SearchVideosResultsPage.as_view(), name='search_videos'),

]