from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Email Address'}))
    first_name = forms.CharField(label='', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter First Name'}))
    last_name = forms.CharField(label='', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'font-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class=""></span>'

        self.fields['password1'].widget.attrs['class'] = 'font-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class=""></span>'

        self.fields['passsword2'].widget.attrs['class'] = 'font-control'
        self.fields['passsword2'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['passsword2'].label = ''
        self.fields['passsword2'].help_text = '<span class=""></span>'

