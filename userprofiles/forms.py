import urllib.parse
from django import forms
# from django.core.files.images import get_image_dimensions
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.http import JsonResponse
from django.forms.widgets import CheckboxInput
from .models import Userprofile, TermUser


# REGISTRATION USER FORM

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            # 'agree',
        ]

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class TermsForm(forms.ModelForm):
    class Meta:
        model = TermUser
        fields = [
            'agree',
        ]

        widgets = {
            'agree': CheckboxInput(attrs={'class': 'agree'}),
        }


# -- EDIT FORM IN PROFILE -- #

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Userprofile
        fields = [
            'avatar',
            'picture',
            'title',
            'company_name',
            'industry',
            'description',
            'country',
            'city',
            'locations',
            'employment',
            'business',
            'purpose',
        ]
