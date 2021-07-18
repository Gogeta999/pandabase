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

class CourseTag(models.Model):
    course_id = models.AutoField(primary_key= True)
    course_tag = models.CharField(max_length=50, unique=True)
    course_num = models.IntegerField(null= False)
    
    def __str__(self):
        return self.course_tag

class CourseName(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name


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

    class Meta:
        ordering = ["-date_uploaded"]

    def __str__(self):
        return self.video_name
    
