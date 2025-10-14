from django.shortcuts import render

# Create your views here.
def lesson1_tutorial(request):
  return (
    render(request,'lesson1/django_lesson1_basics.html',{})
  )