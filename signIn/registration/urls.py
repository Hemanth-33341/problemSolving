from django.urls import path
from . import views

urlpatterns=[
            path('',views.home,name='home'),
            path('register/',views.register,name='register'),
            path('log_in/',views.log_in,name='log_in'),
            path('welcome/',views.welcome,name='welcome')
]