from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.conf import settings
import os
from django.dispatch import receiver
from django.db.models.signals import post_save


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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default = GENDER_CHOICES[3])
    bio = models.CharField(max_length= 200,blank=True,null=True)

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
    course_num = models.IntegerField(null= True, unique= True,blank=True)
    course_thumbnail = models.FileField(upload_to= course_thumbnail_path,default='/default/default-course.jpg')
    def __str__(self):
        return str(self.course_tag)




def video_path(instance,filename):
    ext = filename.split('.')[-1]
    return os.path.join('course_videos/',instance.course_name.course_name, filename)

def video_thumbnails_path(instance,filename):
    ext = filename.split('.')[-1]
    return os.path.join('course_videos/',instance.course_name.course_name, 'thumbnails/',filename)

class Video(models.Model):
    video_id = models.AutoField(primary_key= True)
    uploaded_author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    course_name = models.ForeignKey(CourseName, on_delete= models.PROTECT)
    video_name = models.CharField(max_length=50)
    course_tag = models.ManyToManyField(CourseTag, blank= False)
    video_file = models.FileField(upload_to= video_path,blank=True,null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    video_thumbnail = models.ImageField(upload_to = video_thumbnails_path, default = '/default/default-video.jpg')
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

@receiver(post_save, sender= CourseName)
def create_courseTag(sender, instance, created, **kwargs):
	if created:
		CourseTag.objects.create(course_tag=instance)
@receiver(post_save, sender= CourseName)
def save_courseTag(sender, instance, **kwargs):
	instance.coursetag.save()


@receiver(post_save, sender= User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance,nickname=instance.username,email=instance.email,gender='H')
            
@receiver(post_save, sender= User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
    
