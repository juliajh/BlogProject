from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path

urlpatterns=[
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
]