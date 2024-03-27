"""
URL configuration for acads project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
       path('login1', views.login1,name="login"),
    path('add_course', views.courseform,name="courseform"),
     path('social-auth/', include('social_django.urls', namespace='social')),
    path('display', views.display,name="display"),
    path('edit_profile', views.edit_profile,name="edit_profile"),
    path('allcourses', views.allcourses,name="allcourses"),
    path('', views.initial,name="initial"),
    path('add_content', views.add_content,name="add_content"),
    path('evaluation', views.evaluations,name="evaluation"),
  path('marks/<str:profile_id>/', views.marks2, name="marks"),
    path('download/<int:pk>/', views.download, name="download"),
      path('grades', views.courses1,name="allgrades"),
      path('add_grading/<str:profile_id>/', views.add_grading, name="add_grading"),
path('announcements', views.announcements,name="announcements"),
path('try1', views.try1,name="try1"),
path('add_cart/<int:pk>/', views.add_cart,name="add_cart"),
path('display2', views.display2,name="display2"),
path('see_grades', views.see_grades,name="see_grades"),
path('loginf', views.loginf,name="loginf"),
path('tut', views.tutform,name="tut"),
path("add_tut",views.moderator,name="add_tut"),
path("tut2",views.add_to_tut,name="tut2")




]
