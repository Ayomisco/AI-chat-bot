from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}), max_length=30, required=True)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class':'form-control form-control-lg'}), max_length=100, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }