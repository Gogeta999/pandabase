from django.db import models
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic import FormView, TemplateView
from django.views.generic.detail import DetailView
from .models import CourseTag, Video, User, Profile, PurchasedCourse
from django.urls import reverse_lazy
from .forms import  SearchVideosForm
from django.utils import timezone
from django.db.models import Q
from django.urls import resolve
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
class Index(DetailView, FormView):
    template_name = 'main/index.html'
    form_class = SearchVideosForm
    model = PurchasedCourse
    
    def get_object(self):
        if 'pk' not in self.kwargs:
            return PurchasedCourse.objects.last()
        return super(Index, self).get_object()

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        context['demo_videos'] = Video.objects.all()
        return context

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
    def get_context_data(self, **kwargs):
        context = super(CourseVideoPage, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['courses'] = PurchasedCourse.objects.get(user= self.request.user.profile)
            return context
        else:
            return context
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return 'main/course_video.html'
        else:
            return 'main/course_demo_video.html'
  
def courseVideoPage(request, pk):
    video = get_object_or_404(Video, pk=pk)
    # video = Video.objects.get(pk = pk)
    # context["valid"] = tag
    if request.user.is_authenticated:
        purchasedCourse = PurchasedCourse.objects.get(user= request.user.profile)
        video_tags = video.course_tag.all
        purchasedCourse_tag = purchasedCourse.course.all
        context ={}
        context["video"] = video
        context["courses"] = purchasedCourse
        context["video_tags"] = video_tags
        context["purchasedCourse_tag"] = purchasedCourse_tag
        # if not video:
        #     raise Http404("Does not exist")
        return render(request, 'main/course_video.html', context)
    else:
        context ={}
        context["video"] = video
        return render(request, 'main/course_demo_video.html', context)

class CourseDemoVideoPage(generic.DetailView):
    model = Video
    template_name = 'main/course_demo_video.html'
    def get_context_data(self, **kwargs):
        context = super(CourseDemoVideoPage, self).get_context_data(**kwargs)
        context['courses'] = PurchasedCourse.objects.all()
        return context

    

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


