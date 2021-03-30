from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
#Here we create the views for the forms

class Main_page_form(forms.Form):
    request_objective = forms.ChoiceField(choices=(("1","Recipe"),("2","BasicProduct"),("3","Nutrient")),widget=forms.RadioSelect,label='')
    item_name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Type something here'}))


class Create_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


