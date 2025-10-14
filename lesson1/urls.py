from django.urls import path
from . import views

urlpatterns = [
  path('',views.lesson1_tutorial,name='lesson1_tutorial')
]