from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseNotAllowed,HttpResponseNotFound
from .models import *
from .forms import Main_page_form, Create_user_form
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='/login/')
def main_url(req):
    template_name="DishDecoderApp/main_url.html"
    template_data = {}
    if req.method == 'GET':
        form = Main_page_form()
        template_data['form']=form
        template_data['login_button_link']="/login/"
        template_data['search_form_link']="/search/"
        template_data['create_receip_link']="/create/"
        return render(req, template_name,template_data)
    return HttpResponseBadRequest()


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
    redirect('/')
