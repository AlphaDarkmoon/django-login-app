from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms

# Custom form for creating new users, inheriting from UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # Specify the fields to be displayed and filled in the form
        fields = ("email", "first_name", "last_name", "phone", "country", "address")
        # Add placeholder attributes for the email input field
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "Email address"}),
        }
    
    # Define individual form fields with placeholder attributes
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "First name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Last name"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Phone"}))
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Country"}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Address"}))

# Custom form for editing user details, inheriting from UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # Specify the fields to be displayed and edited in the form
        fields = ("email",)
