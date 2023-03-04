from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def default_response(request):
    empl1 = Employee.objects.get(id=1)
    return render(request, 'index.html', {'name': empl1.name, 'points': empl1.points})
