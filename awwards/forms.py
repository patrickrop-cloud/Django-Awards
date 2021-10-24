from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProjectForm(forms.ModelForm):
    class Meta:
        model =  Project
        exclude = ['username', 'design', 'usability', 'creativity','overall_score','screenshot2','screenshot3']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']