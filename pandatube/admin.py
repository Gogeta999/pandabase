from django.contrib import admin
from .models import User, Profile, CourseTag,CourseName, Video
# Register your models here.


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(CourseTag)
admin.site.register(CourseName)
admin.site.register(Video)
