from django.urls import path, register_converter
from django.contrib.auth.decorators import login_required, permission_required
from . import views
from utils import HashIdConverter

register_converter(HashIdConverter, "hashid")

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path(r'<int:pk>/', views.UnloginIndex.as_view(),name='login-index'),
    path(r'profile/<int:pk>/', views.UserProfilePage.as_view(), name='profile'),
    path(r'course<int:coursenum>/<hashid:pk>/', login_required(views.CoursePage.as_view()), name='course'),
    path(r'course/video/<hashid:pk>/', views.CourseVideoPage.as_view(), name='video'),
    path('search', login_required(views.SearchVideosResultsPage.as_view()), name='search_videos'),

]
