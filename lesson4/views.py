from django.shortcuts import render

# Create your views here.
def lesson4_tutorial(request):
  return (
    render(request,'lesson4/django_lesson4_templates_static.html',{})
  )
