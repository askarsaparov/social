from django.urls import path

from apps.musker.views import home, profile_list, profile

urlpatterns = [
    path('', home, name='home'),
    path('profile-list/', profile_list, name='profile-list'),
    path('profile/<int:pk>/', profile, name='profile'),
]