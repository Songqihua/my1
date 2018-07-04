from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import Users
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def index(request):
    

    return render(request,'myadmin/index.html')


