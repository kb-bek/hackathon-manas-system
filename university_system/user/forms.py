from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'father_name', 'date_of_birth',
            'gender', 'citizenship', 'email', 'phone_number', 'password']