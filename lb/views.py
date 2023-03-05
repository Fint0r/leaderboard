from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.


def default_response(request):
    empl1 = Employee.objects.get(id=1)
    return render(request, 'index.html', {'name': empl1.name, 'points': empl1.points, 'picLocation': empl1.picture_location})


def get_client_ip(request):  # not working
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
