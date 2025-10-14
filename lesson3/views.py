from django.shortcuts import render

# Create your views here.
def lesson3_tutorial(request):
  return render(request,'lesson3/django_lesson3_urls_views'
  '.html',{})