from django.contrib import admin
from .models import User, Profile, CourseTag,CourseName, Video,PurchasedCourse
from .forms import AdminCustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = AdminCustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        # (
        #     'User Status',
        #     {
        #         'fields': (
        #             'vip_levels',
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

