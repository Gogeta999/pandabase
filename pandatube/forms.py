from typing import Sequence
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User
from django.core.exceptions import ValidationError
# class UserLoginForm(forms.Form):
#     username = forms.CharField(label="UserName", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# class AdminCustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField()
#     #If created on web
#     def clean_email(self):
#        email = self.cleaned_data.get('email')
#        if User.objects.filter(email=email).exists():
#             raise ValidationError("This email already used")
#        return self.cleaned_data

#     class Meta:
#         model = User
#         fields = "__all__"

class UserProfileUpdateForm(forms.Form):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown'),
        ('H', 'Anonymous'),
    )
    nickname = forms.CharField(label="UserName", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", max_length=128, widget=forms.EmailInput(attrs={'class': 'form-control','readonly': 'readonly'}))
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    bio = forms.CharField(label="Bio", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
  
    class Meta:
        model=Profile
        # fields = "__all__"
        fields=['nickname','email','gender','bio']
    # def save(self, request, commit=True):
    #     user = request.user
    #     data = self.cleaned_data
    
    # def update_profile(self, commit=True):
    #     user = super(UserProfileUpdateForm, self).save(commit=False)
    #     nickname = self.cleaned_data["nickname"]
    #     email = self.cleaned_data["email"]
    #     gender = self.cleaned_data["gender"]
    #     bio = self.cleaned_data["bio"]
    #     user.nickname = nickname
    #     user.email = email
    #     user.gender = gender
    #     user.bio = bio
    #     if commit:
    #         user.save()
    #     return user

class SearchVideosForm(forms.Form):
    q = forms.CharField(label='', max_length= 50, widget= forms.TextInput(attrs={'placeholder': 'Search Videos','class': 'form-control','type': 'search'}))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length= 50, widget= forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1', 'password2')
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.TextInput(attrs={'class': 'form-control'}),
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