from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path(r'profile/<int:pk>/', views.UserProfilePage.as_view(), name='profile'),
    path(r'course/<int:pk>/', login_required(views.CoursePage.as_view()), name='course'),
    # path(r'course/video/<int:pk>/t', views.CourseVideoPage.as_view(), name='video-t'),
    path(r'course/video/<int:pk>/', views.courseVideoPage, name='video'),
    path('search', login_required(views.SearchVideosResultsPage.as_view()), name='search_videos'),

]