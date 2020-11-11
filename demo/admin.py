from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from .models import Question, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profiles'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = (
        "id", "username", "email", 'first_name', 'last_name', 'last_login', 'date_joined', "profile_description")

    def profile_description(self, obj):
        return obj.userprofile.description

    profile_description.short_description = 'Description'


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Question)
