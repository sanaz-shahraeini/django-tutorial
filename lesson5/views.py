from django.shortcuts import render

# Create your views here.
def lesson5_tutorial(request):
  return render(request,'lesson5/django_lesson5_templates_static_summary.html',{})