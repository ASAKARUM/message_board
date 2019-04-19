from django.urls import path
from . import views, auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', auth_views.login, name='login'),
    path('register', auth_views.register, name='register'),
    path('authenticate', auth_views.authenticate, name='authenticate'),
    path('logout', auth_views.logout, name='logout'),
    path('newform', auth_views.newform, name="newform"),
    path('changelikes', auth_views.changelikes, name="changelikes")
]
