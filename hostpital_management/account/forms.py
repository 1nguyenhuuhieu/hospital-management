from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import *


class RegisterForm(UserCreationForm):
    password2 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={
        'autocomplete':'new-password'}))
    password1 = forms.CharField(widget=forms.HiddenInput)
    email = forms.CharField(label='Email', widget=forms.HiddenInput)
    username = forms.EmailField(label='Email', help_text="Địa chỉ email sẽ được dùng làm tên đăng nhập", widget=forms.EmailInput(attrs={
        'autocomplete':'off'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["user", "full_name", "avatar"]