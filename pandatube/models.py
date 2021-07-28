from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.conf import settings
import os
class User(AbstractUser):
    email = models.EmailField(unique=True,blank=True)

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown'),
        ('H', 'Anonymous')
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    nickname = models.CharField(max_length= 8, unique= True)
    email = models.EmailField(blank= True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bio = models.CharField(max_length= 200, )
    def __str__(self):
        return self.user.get_username()
class CourseName(models.Model):
    course_name = models.CharField(max_length=50, unique= True)

    def __str__(self):
        return self.course_name


def course_thumbnail_path(instance,filename):
    ext = filename.split('.')[-1]
    return os.path.join('course_thumbnail/',str(instance.course_tag),filename)
class CourseTag(models.Model):
    course_id = models.AutoField(primary_key= True)
    course_tag = models.OneToOneField(CourseName,on_delete= models.PROTECT,unique=True)
    course_num = models.IntegerField(null= False, unique= True)
    course_thumbnail = models.FileField(upload_to= course_thumbnail_path,default='/default/default-course.jpg')
    def __str__(self):
        return str(self.course_tag)




def video_path(instance,filename):
    ext = filename.split('.')[-1]
    return os.path.join('course_videos/',instance.course_name.course_name,filename)

class Video(models.Model):
    video_id = models.AutoField(primary_key= True)
    uploaded_author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    course_name = models.ForeignKey(CourseName, on_delete= models.PROTECT)
    video_name = models.CharField(max_length=50)
    course_tag = models.ManyToManyField(CourseTag, blank= False)
    video_file = models.FileField(upload_to= video_path,blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this Video."""
        return reverse('video', args=[str(self.video_id)])
    # def get_file_path(self):
    #     return video_path
    class Meta:
        ordering = ["-date_uploaded"]

    def __str__(self):
        return self.video_name

class PurchasedCourse(models.Model):
    user = models.OneToOneField(Profile,on_delete=models.PROTECT)
    course = models.ManyToManyField(CourseTag,blank=True,related_name='courses')

    # def course_names(self):
    #     return ', '.join([a.course_names for a in self.course.all()])
    # course_names.short_description = "Course Names"
    def __str__(self):
        return str(self.user) + '\'s Purchased Course'
    
