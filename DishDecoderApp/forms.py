from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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

class Change_password_form(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password','new_password2']

class Change_email_form(forms.Form):
    new_email1 = forms.EmailField(label="New email address",widget=forms.EmailInput)
    new_email2 = forms.EmailField(label="New email confirmation",widget=forms.EmailInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(Change_email_form,self).__init__(*args,**kwargs)

    def clean_new_email1(self):
        old_email = self.user.email
        new_email1 = self.cleaned_data.get('new_email1')
        if new_email1 and old_email:
            if new_email1 == old_email:
                raise forms.ValidationError("This email address its already define",code="Same email")
        return new_email1

    def clean_new_email2(self):
        new_email1 = self.cleaned_data.get('new_email1')
        new_email2 = self.cleaned_data.get('new_email2')
        if new_email1 and new_email2:
            if new_email1 != new_email2:
                raise forms.ValidationError("The emails you have written do not match",code="mismatch")
        return new_email2

    def save(self, commit=True):
        email = self.cleaned_data["new_email1"]
        self.user.email = email
        if commit:
            self.user.save()
        return self.user
    class Meta:
        fields = ['new_email1','new_email2']

class Create_recipe_form(forms.Form):
    steps = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Separe the steps using #'}))
    basicproduct = forms.ModelMultipleChoiceField(queryset=BasicProducts.objects.all(), widget=forms.CheckboxSelectMultiple())
    nutrients = forms.ModelMultipleChoiceField(queryset=Nutrients.objects.all(), widget=forms.CheckboxSelectMultiple())




