from django.shortcuts import render, redirect
from awwards.models import Profile, Project
from .forms import CreateUserForm,ProfileForm,ProjectForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout as dj_login
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Myprofile,Myprojects
from .serializer import MerchSerializer

# Create your views here.
def index(request):
    projects = Project.objects.all()

    if 'item_name' in request.GET:
        item_name = request.GET['item_name']
        projects = projects.filter(title_icontains=item_name)
    else:
        projects=Project.objects.all()

    return render(request, 'index.html',{'projects':projects})