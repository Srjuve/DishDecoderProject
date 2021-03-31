from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseNotAllowed,HttpResponseNotFound
from .forms import Main_page_form, Create_user_form
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from urllib.parse import urlencode
from DishDecoderApp.models import *
# Create your views here.

def main_url(req):
    template_name="DishDecoderApp/main.html"
    template_data = {}
    if req.method == 'POST':
        radioptchoice = str(req.POST.get('request_objective'))
        searched_data = str(req.POST.get('item_name'))
        query_string = urlencode({'search':searched_data})
        if radioptchoice == '1':
            base_url = '/recipes/'
        elif radioptchoice == '2':
            base_url = '/basicproducts/'
        elif radioptchoice == '3':
            base_url = '/nutrients/'
        url = '{}?{}'.format(base_url,query_string)
        return redirect(url)
    form = Main_page_form()
    template_data['form']=form
    template_data['login_button_link']="/login/"
    template_data['logout_button_link']="/logout/"
    template_data['profile_form_link']="/profile/"
    template_data['create_receip_link']="/create/"
    return render(req, template_name,template_data)


def register_page_url(req):
    template_data={}
    form = Create_user_form()
    if req.method == 'POST':
        form = Create_user_form(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
   
    template_data['reg_form']=form
    template_data['login_button_link']="/login/"
    template_data['home_button_link']="/"
    template_name="DishDecoderApp/register.html"
    return render(req, template_name,template_data)


def login_page_url(req):
    if not req.user.is_authenticated:
        template_data={}
        template_name="DishDecoderApp/login.html"
        form = AuthenticationForm()
        if req.method=='POST':
            username = req.POST.get('username')
            password = req.POST.get('password')
            user = authenticate(req,username=username,password=password)
            if user is not None:
                login(req,user)
                return redirect('/')
            else:
                messages.warning(req,'Login credentials invalid')
        template_data['auth_form']=form
        template_data['home_button_link']="/"
        template_data['register_button_link']="/register/"
        return render(req, template_name,template_data)
    else:
        return redirect('/')

def logout_url(req):
    if req.user.is_authenticated:
        logout(req)
    return redirect('/')

def list_recipes_url(req):
    return list_data(req,"DishDecoderApp/recipes.html","/recipe/",Recipes)

def list_basicproducts_url(req):
    return list_data(req,"DishDecoderApp/basicproducts.html","/basicproduct/",BasicProducts)

def list_nutrients_url(req):
    return list_data(req,"DishDecoderApp/nutrient.html","/nutrient/",Nutrients)

def list_data(req,template_name,baseurl,searchedObject):
    template_data={}
    searched_name=req.GET.get('search')
    if searched_name is not None:
        data_fields = searchedObject.objects.filter(name__contains=searched_name)
        if data_fields.count()==1:
            url=baseurl+str(getattr(data_fields.first(),'id'))
            return redirect(url)
        template_data["listedtuples"]=data_fields
        return render(req,template_name,template_data)
    else:
        return HttpResponseBadRequest()


def recipe_profile_url(req, recipeid):
    return HttpResponse('Placeholder')

def basicproduct_profile_url(req, basicproductid):
    return HttpResponse('Placeholder')

def nutrient_profile_url(req, nutrientid):
    return HttpResponse('Placeholder')