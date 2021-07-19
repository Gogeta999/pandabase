from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# class UserLoginForm(forms.Form):
#     username = forms.CharField(label="UserName", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length= 50, widget= forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','password1', 'password2')
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "password1": forms.TextInput(attrs={'class': 'form-control'}),
            "password2": forms.TextInput(attrs={'class': 'form-control'}),
        }
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        email = self.cleaned_data["email"]
        user.email = email
        if commit:
            user.save()
        return user