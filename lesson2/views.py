from django.shortcuts import render

# Create your views here.
def lesson2_tutorial(request):
  return render(request,'lesson2/django_lesson2_project_settings_urls.html',{})