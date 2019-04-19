from django import forms
from .models import Post

class UserForm(forms.Form):
    username = forms.CharField(label='请输入用户名', max_length=30)
    password = forms.CharField(label='请输入密码', widget=forms.PasswordInput())
