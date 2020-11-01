from django.contrib.auth import authenticate
from django.forms import Textarea, ImageField
from django.utils.translation import gettext_lazy as _

from .models import User, Post

from django import forms


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    date_of_birth = forms.DateField(widget=DateInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'password', 'password2',
                  'date_of_birth']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_birthday(self):
        cd = self.cleaned_data
        user_age = cd['date_of_birth']
        age = user_age.year
        if age > "2010":
            raise forms.ValidationError("you are not eligible")
        return cd['date_of_birth']


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'image']
        widgets = {
            'body': Textarea(attrs={'class': 'status-field', 'placeholder': "what's on your mind?"}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'custom-file-input'})
