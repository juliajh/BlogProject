from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *

urlpatterns=[
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    path('register/',register_view,name="signup")
]