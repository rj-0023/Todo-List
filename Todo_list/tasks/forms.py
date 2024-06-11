from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

from .models import TaskModel

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = TaskModel
        fields = [
            'task_name',
            'due_date',
            'notes',
            'status',
        ]

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2' 
        ]