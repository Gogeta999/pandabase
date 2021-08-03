from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import User, Profile, CourseTag,CourseName, Video,PurchasedCourse
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    # add_form = AdminCustomUserCreationForm
    list_display = ('username','email')
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email','password1','password2')
        }),
    )
  
    fieldsets = (
        *UserAdmin.fieldsets,
        # (
        #     'User Email',
        #     {
        #         'fields': (
        #             'email',
        #         )
        #     }
        # )
    )
# Register your models here.
admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(CourseTag)
admin.site.register(CourseName)
admin.site.register(Video)
admin.site.register(PurchasedCourse)

