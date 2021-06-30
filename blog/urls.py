from django.contrib import admin
from django.urls import path,include
from .views import *
import blog.views

urlpatterns = [
    path('<int:blog_id>', blog.views.detail, name='detail'),\
    path('new/',blog.views.new,name="new"),
    path('create/',blog.views.create,name="create"),
    path('delete/<str:id>',blog.views.delete,name="delete"),
    path('edit/<str:id>',blog.views.edit,name="edit"),
    path('update/<str:id>',blog.views.update,name="update"),
] 