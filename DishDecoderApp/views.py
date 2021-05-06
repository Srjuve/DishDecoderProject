from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseNotAllowed,HttpResponseNotFound
from .forms import Main_page_form, Create_user_form, Change_password_form , Change_email_form
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.views.defaults import *
from urllib.parse import urlencode
from DishDecoderApp.models import *
import random


# GET: Show the principal page, and redirects the search depending on what the user selects
class main_url(View):
    template_data = {}
    template_name = "DishDecoderApp/main.html"
    form = Main_page_form()
    def get(self,req):
        self.template_data['form']=self.form
        self.template_data['title_page']='Dish Decoder'
        return render(req, self.template_name,self.template_data)

    def post(self,req):
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

    
#def main_url(req):
#    template_name="DishDecoderApp/main.html"
#    template_data = {}
#    if req.method == 'POST':
#        radioptchoice = str(req.POST.get('request_objective'))
#        searched_data = str(req.POST.get('item_name'))
#        query_string = urlencode({'search':searched_data})
#        if radioptchoice == '1':
#            base_url = '/recipes/'
#        elif radioptchoice == '2':
#            base_url = '/basicproducts/'
#        elif radioptchoice == '3':
#            base_url = '/nutrients/'
#        url = '{}?{}'.format(base_url,query_string)
#        return redirect(url)
#    form = Main_page_form()
#    template_data['form']=form
#    template_data['title_page']='Dish Decoder'
#    return render(req, template_name,template_data)

#GET : shows the registrations form
#POST : proves that the data introduced is correct, creates the user and redirects the user to log in page

class register_page_url(View):
    template_data = {}
    template_name = "DishDecoderApp/register.html"
    form = Create_user_form()
    def get(self, req):
        if not req.user.is_authenticated:
            self.template_data['reg_form']=self.form
            self.template_data['title_page']='Register'
            return render(req, self.template_name,self.template_data)
        return redirect('/')

    def post(self, req):
        if not req.user.is_authenticated:
            if req.method == 'POST':
                form = Create_user_form(req.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/login/')
                else:
                    messages.add_message(req, messages.ERROR, 'Error al registrar-se')
                    self.template_data['reg_form'] = self.form
                    self.template_data['title_page'] = 'Register'
                    return render(req, self.template_name,self.template_data)
        return redirect('/')

#def register_page_url(req):
#    if not req.user.is_authenticated:
#        template_data={}
#        template_name="DishDecoderApp/register.html"
#        form = Create_user_form()
#        if req.method == 'POST':
#            form = Create_user_form(req.POST)
#            if form.is_valid():
#                form.save()
#                return redirect('/login/')
#    
#        template_data['reg_form']=form
#        template_data['title_page']='Register'
#        return render(req, template_name,template_data)
#    return redirect('/')

# GET: Shows the log in forms
# POST: Proves that the data introduced is from an user, autenticates the user and redirects him to the main page logged.
class login_page_url(View):
    template_data={}
    template_name="DishDecoderApp/login.html"
    form = AuthenticationForm()
    def get(self, req):
        if not req.user.is_authenticated:
            self.template_data['auth_form']=self.form
            self.template_data['title_page']='Log in'
            return render(req, self.template_name,self.template_data)
        return redirect('/')
    
    def post(self, req):
        if not req.user.is_authenticated:
            username = req.POST.get('username')
            password = req.POST.get('password')
            user = authenticate(req,username=username,password=password)
            if user is not None:
                login(req,user)
                return redirect('/')
            else:
                messages.warning(req,'Login credentials invalid')
                self.template_data['auth_form']=self.form
                self.template_data['title_page']='Log in'
                return render(req, self.template_name,self.template_data)
        return redirect('/')


#def login_page_url(req):
#    if not req.user.is_authenticated:
#        template_data={}
#        template_name="DishDecoderApp/login.html"
#        form = AuthenticationForm()
#        if req.method=='POST':
#            username = req.POST.get('username')
#            password = req.POST.get('password')
#            user = authenticate(req,username=username,password=password)
#            if user is not None:
#                login(req,user)
#                return redirect('/')
#            else:
#                messages.warning(req,'Login credentials invalid')
#        template_data['auth_form']=form
#        template_data['title_page']='Log in'
#        return render(req, template_name,template_data)
#    else:
#        return redirect('/')

# GET: the user log outs

class logout_url(View):
    def get(self, req):
        if req.user.is_authenticated:
            logout(req)
        return redirect('/')

#def logout_url(req):
#    if req.user.is_authenticated:
#        logout(req)
#    return redirect('/')

# GET: the user profile where the user can go to change the password or the email
class user_profile_url(LoginRequiredMixin, View):
    login_url = '/login/'
    template_data = {}
    template_name = "DishDecoderApp/user_profile.html"
    def get(self, req):
        if Ratings.objects.filter(id_autor=req.user.id).exists():
            rating_data=Ratings.objects.filter(id_autor=req.user.id).all()
            self.template_data['scored_recipes']=rating_data
        self.template_data['title_page']='User profile'
        return render(req, self.template_name, self.template_data)

#@login_required(login_url='/login/')
#def user_profile_url(req):
#    template_data = {}
#    template_name = "DishDecoderApp/user_profile.html"
#    if Ratings.objects.filter(id_autor=req.user.id).exists():
#        rating_data=Ratings.objects.filter(id_autor=req.user.id).all()
#        template_data['scored_recipes']=rating_data
#    template_data['title_page']='User profile'
#    return render(req, template_name,template_data)


class change_data_url(LoginRequiredMixin, View):
    login_url = '/login/'
    template_data={}
    template_name=""
    form_function=Change_password_form
    title_page=""

    def get(self, req):
        self.template_data['change_data_form']=self.form_function(req.user)
        self.template_data['title_page']='Change password'
        return render(req, self.template_name, self.template_data)


    def post(self, req):
        form = self.form_function(req.user,req.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
        else:
            messages.warning(req,'Invalid data entered')
        self.template_data['change_data_form']=self.form_function(req.user)
        self.template_data['title_page']='Change password'
        return render(req, self.template_name, self.template_data)

#GET: Show the password change form
#POST: Fill form with post data, validate it and, if valid, save it into the database
#@login_required(login_url='/login/')
#def change_password_url(req):
#    return change_user_data(req,'DishDecoderApp/change_password.html',Change_password_form)



#GET: Show the email change form
#POST: Fill form with post data, validate it and, if valid, save it into the database

#@login_required(login_url='/login/')
#def change_mail_url(req):
#    return change_user_data(req,'DishDecoderApp/change_email.html',Change_email_form)

# funcion used by change mail and change password to perform each funtions
#@login_required(login_url='/login/')
#def change_user_data(req,template_name,form_function):
#    template_data={}
#    if req.method=='POST':
#        form = form_function(req.user,req.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('/profile/')
#        else:
#            messages.warning(req,'Invalid data entered')
#    template_data['change_data_form']=form_function(req.user)
#    if template_name =='DishDecoderApp/change_password.html':
#        template_data['title_page']='Change Password'
#    if template_name == 'DishDecoderApp/change_email.html':
#        template_data['title_page']='Change email'
#    return render(req, template_name, template_data)

class list_data_url(View):
    template_data={}
    template_name=""
    baseurl=""
    searchedObject=Recipes
    title_page=""

    def get(self, req):
        template_data={}
        searched_name=req.GET.get('search')
        if searched_name is not None:
            data_fields = self.searchedObject.objects.filter(name__contains=searched_name)
            if data_fields.count()==1:
                url=self.baseurl+str(getattr(data_fields.first(),'id'))
                return redirect(url)
            template_data["listedtuples"]=data_fields
            template_data['title_page']=self.title_page
            return render(req,self.template_name,template_data)
        else:
            return bad_request(req, exception=None)

# GET: funtions that use the funtion list_data to list the recipes
#def list_recipes_url(req):
#    return list_data(req,"DishDecoderApp/recipes.html","/recipe/",Recipes)

# GET: funtions that use the funtion list_data to list the basic products
#def list_basicproducts_url(req):
#    return list_data(req,"DishDecoderApp/basicproducts.html","/basicproduct/",BasicProducts)

# GET: funtions that use the funtion list_data to list the nutrients
#def list_nutrients_url(req):
#    return list_data(req,"DishDecoderApp/nutrients.html","/nutrient/",Nutrients)

#GET: funtion thah shows the list of recipes, basic products or nutrients that start by the same way that the user typed
#def list_data(req,template_name,baseurl,searchedObject):
#    template_data={}
#    searched_name=req.GET.get('search')
#    if searched_name is not None:
#        data_fields = searchedObject.objects.filter(name__contains=searched_name)
#        if data_fields.count()==1:
#            url=baseurl+str(getattr(data_fields.first(),'id'))
#            return redirect(url)
#        template_data["listedtuples"]=data_fields
#        if template_name =="DishDecoderApp/recipes.html":
#            template_data['title_page']='Recipes'
#        if template_name == "DishDecoderApp/basicproducts.html":
#            template_data['title_page']='Basic Products'
#        if template_name == "DishDecoderApp/nutrients.html":
#            template_data['title_page']='Nutrients'
#        return render(req,template_name,template_data)
#    else:
#        return bad_request(req, exception=None)

class recipe_profile_url(View):

    def get(self, req, recipeid):
        template_data={}
        try :
            recipe = Recipes.objects.get(id=recipeid)
            rec_prod = Recipe_Product.objects.filter(id_recipe=recipeid)

            nutrients = Nutrients.objects.all()

            res = self.get_nutritional_value_foreach_nutrition(rec_prod)
            steps = recipe.steps.strip().split('#')
            steps = [x for x in steps if x.strip()]

            rating_data = Ratings.objects.filter(id_recipe=recipeid).all()
            try:
                average = sum([recipe_rating.rating for recipe_rating in rating_data]) / rating_data.count()
            except ZeroDivisionError as e:
                average = "Not rated"

            template_data['steps'] = steps
            template_data['recipe'] = recipe
            template_data['rec_prod'] = rec_prod
            template_data['nut_value'] = res
            template_data['rating_data'] = rating_data
            template_data['average_score'] = average
            template_data['title_page']='Recipe Profile'
            template_name="DishDecoderApp/recipe.html"  
            return render(req, template_name,template_data)
        except Recipes.DoesNotExist:
            return page_not_found(req, exception=None)
    
    def get_nutritional_value_foreach_nutrition(self,rec_prod):
        nut_value = {} 
        for rel_rec_prod in rec_prod:
            for rel_prod_nut in Product_Nutrients.objects.filter(id_product=rel_rec_prod.id_product):
                unit = rel_rec_prod.id_product.unit
                value = rel_rec_prod.quantity * (rel_prod_nut.quantity / 100)
                nut_id = rel_prod_nut.id_nutrient.id
                if unit == 'L':
                    value *= 1000
                if nut_id not in nut_value:
                    nut_value[nut_id] = {'value':value, 'nutrient' : rel_prod_nut.id_nutrient}
                else:
                    nut_value[nut_id]['value'] += value
        return [list(total_nut_val.values()) for total_nut_val in nut_value.values()]

# GET: shows the recipe page with the relationated info about it
#def recipe_profile_url(req, recipeid):
#    template_data={}
#    try :
#        recipe = Recipes.objects.get(id=recipeid)
#        rec_prod = Recipe_Product.objects.filter(id_recipe=recipeid)

#        nutrients = Nutrients.objects.all()

#        res = get_nutritional_value_foreach_nutrition(rec_prod)
#        steps = recipe.steps.strip().split('#')
#        steps = [x for x in steps if x.strip()]

#        rating_data = Ratings.objects.filter(id_recipe=recipeid).all()
#        try:
#            average = sum([recipe_rating.rating for recipe_rating in rating_data]) / rating_data.count()
#        except ZeroDivisionError as e:
#            average = "Not rated"

#        template_data['steps'] = steps
#        template_data['recipe'] = recipe
#        template_data['rec_prod'] = rec_prod
#        template_data['nut_value'] = res
#        template_data['rating_data'] = rating_data
#        template_data['average_score'] = average
#        template_data['title_page']='Recipe Profile'
#        template_name="DishDecoderApp/recipe.html"  
#        return render(req, template_name,template_data)
#    except Recipes.DoesNotExist:
#       return page_not_found(req, exception=None)
    
    
    
# GET: Calculates the nutritional value from a recipe
#def get_nutritional_value_foreach_nutrition(rec_prod):
#    nut_value = {} 
#    for rel_rec_prod in rec_prod:
#        for rel_prod_nut in Product_Nutrients.objects.filter(id_product=rel_rec_prod.id_product):
#            unit = rel_rec_prod.id_product.unit
#            value = rel_rec_prod.quantity * (rel_prod_nut.quantity / 100)
#            nut_id = rel_prod_nut.id_nutrient.id
#            if unit == 'L':
#                value *= 1000
#            if nut_id not in nut_value:
#                nut_value[nut_id] = {'value':value, 'nutrient' : rel_prod_nut.id_nutrient}
#            else:
#                nut_value[nut_id]['value'] += value
#    return [list(total_nut_val.values()) for total_nut_val in nut_value.values()]


# GET: Shows the basic product and the data related to them
class basicproduct_profile_url(View):
    def get(self, req, basicproductid):
        template_data={}
        template_name="DishDecoderApp/basic_product.html"        
        try:
            productData=BasicProducts.objects.get(id=basicproductid)
            recipesData=Recipe_Product.objects.filter(id_product=basicproductid).all()
            if(recipesData.count()>=5):
                template_data["recipes_products"]= random.sample(list(recipesData),5)
            else:
                template_data["recipes_products"] = recipesData

            template_data["basic_product"] = productData
            template_data['title_page']='Basic Product Profile'
            return render(req,template_name,template_data)
        except BasicProducts.DoesNotExist:
            return page_not_found(req, exception=None)


#def basicproduct_profile_url(req, basicproductid):
#    template_data={}
#    template_name="DishDecoderApp/basic_product.html"        
    
#    try:
#        productData=BasicProducts.objects.get(id=basicproductid)
#        recipesData=Recipe_Product.objects.filter(id_product=basicproductid).all()
#        if(recipesData.count()>=5):
#            template_data["recipes_products"]= random.sample(list(recipesData),5)
#        else:
#            template_data["recipes_products"] = recipesData

#        template_data["basic_product"] = productData
#        template_data['title_page']='Basic Product Profile'
#        return render(req,template_name,template_data)
    
#    except BasicProducts.DoesNotExist:
#            return page_not_found(req, exception=None)

#GET: shoes the nutrient page and the data related to it
class nutrient_profile_url(View):

    def get(self, req, nutrientid):
        template_data = {}
        try:
            nutr = Nutrients.objects.get(id= nutrientid)
            template_data["nutrient"]=nutr 
            template_name="DishDecoderApp/nutrient.html"
            template_data['title_page']='Nutrient Profile'
            return render(req,template_name,template_data )    
        except Nutrients.DoesNotExist:
            return page_not_found(req, exception=None)

#def nutrient_profile_url(req, nutrientid):
#    template_data = {}
    
#    try:
#        nutr = Nutrients.objects.get(id= nutrientid)
#        template_data["nutrient"]=nutr 
#        template_name="DishDecoderApp/nutrient.html"
#        template_data['title_page']='Nutrient Profile'
#        return render(req,template_name,template_data )    
    
#    except Nutrients.DoesNotExist:
#            return page_not_found(req, exception=None)



class create_recipe_url(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, req):
        return render(req,'DishDecoderApp/createrecipe.html')

# Not implemented
#@login_required(login_url='/login/')
#def create_recipe_url(req):
#    return render(req,'DishDecoderApp/createrecipe.html')


