from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from apps.musker.models import Profile

User = get_user_model()

# UnRegister your models here.
admin.site.unregister(Group)
admin.site.unregister(User)


# Mix Profile info into User info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields on admin page
    fields = ('username',)
    inlines = (ProfileInline,)


admin.site.register(User, UserAdmin)
# admin.site.register(Profile)
