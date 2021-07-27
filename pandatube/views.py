from django.db import models
from django.http import request
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import FormView, TemplateView
from django.views.generic.detail import DetailView
from .models import Video, User, Profile, PurchasedCourse
from django.urls import reverse_lazy
from .forms import  SearchVideosForm
from django.utils import timezone
from django.db.models import Q
from django.urls import resolve
from django.core.cache import cache
class Index(DetailView, FormView):
    template_name = 'main/index.html'
    form_class = SearchVideosForm
    model = PurchasedCourse
    
    def get_object(self):
        if 'pk' not in self.kwargs:
            return PurchasedCourse.objects.last()
        return super(Index, self).get_object()



#Use Login From auth.accounts
# class UserLoginPage(TemplateView):
#     form_class = UserLoginForm
#     template_name = 'registration/login.html'

#Not Necessary to let user register themselves
# class UserRegisterPage(generic.CreateView):
#     form_class = UserRegisterForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('index')

class UserProfilePage(generic.DetailView):
    model = Profile    
    template_name = 'main/profile.html'
    # def get_object(self):
    #     obj = super().get_object()
    #     # Record the last accessed date
    #     obj.last_accessed = timezone.now()
    #     obj.save()
    #     return obj

def course(request, pk):

    videos = Video.objects.all()
    return render(request, 'main/course.html', videos)

class CoursePage(generic.ListView):
    model = Video
    template_name = 'main/course.html'
    def get_context_data(self, *args, **kwargs):
        context = super(CoursePage, self).get_context_data(*args, **kwargs)
        context['course_id'] = self.kwargs['pk']
        return context
    

class CourseVideoPage(generic.DetailView):
    model = Video
    template_name = 'main/course_video.html'

class SearchVideosResultsPage(generic.ListView):
    model = Video
    template_name = 'main/search_results.html'
    form_class = SearchVideosForm
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Video.objects.filter(
            Q(video_name__icontains=query) 
        )
        return object_list


