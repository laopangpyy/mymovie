from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label='密码')
    username = forms.CharField(label = '用户名')
    email = forms.CharField(label='电子邮箱')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


			




		
		


