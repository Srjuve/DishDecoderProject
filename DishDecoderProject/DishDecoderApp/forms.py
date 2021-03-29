from django import forms
#Here we create the views for the forms

class Main_page_form(forms.Form):
    request_objective = forms.ChoiceField(choices=(("1","Recipe"),("2","BasicProduct"),("3","Nutrient")),widget=forms.RadioSelect,label='')
    item_name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Type something here'}))

