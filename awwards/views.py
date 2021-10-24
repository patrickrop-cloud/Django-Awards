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

def registeruser(request):
    title = 'Register - awwards'
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!.  Check out our Email later :)')
            return redirect('login')

        else:
            form = CreateUserForm
        context = {
                'title':title,
                'form':form,
        }
        return render(request, 'registration/register.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

            else:
                messages.info(request, 'Username or password incorrect')

            context = {}
            return render(request, 'registration/login.html', context)