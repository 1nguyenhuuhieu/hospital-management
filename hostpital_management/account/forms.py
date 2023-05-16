from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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