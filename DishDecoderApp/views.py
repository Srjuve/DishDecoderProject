from DishDecoderProject.settings import API_KEY
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseNotAllowed,HttpResponseNotFound
from .forms import Main_page_form, Create_user_form, Change_password_form , Change_email_form, Comments_form
from .forms import *
from django.forms import formset_factory
from .forms import Main_page_form, Create_user_form, Change_password_form , Change_email_form, Autocomplete_form
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.core.exceptions import ValidationError
from django.views.defaults import *
from django.db import *
from urllib.parse import urlencode
from DishDecoderApp.models import *
import random


# GET: Show the principal page, and redirects the search depending on what the user selects
class main_url(View):
    template_name = "DishDecoderApp/main.html"
    form = Main_page_form()
    aform = Autocomplete_form
    def get(self,req):
        template_data = {}
        template_data['form']=self.form
        template_data['aform'] = self.aform
        template_data['title_page']='Dish Decoder'
        template_data['api_key'] = API_KEY
        return render(req, self.template_name,template_data)

    def post(self,req):
        from django.core.exceptions import ValidationError
        external_recipe_title = req.POST.get('recipe_title')
        if external_recipe_title:
            try:
                url = self._autocomplete(req, external_recipe_title)
            except ValidationError:
                return page_not_found(req, exception=None)
        else:
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
    
    def _autocomplete(self, req, external_recipe_title):
        from django.core.validators import URLValidator
        external_recipe_href = req.POST.get('recipe_href')
        external_recipe_ing = req.POST.get('recipe_ing')

        validate = URLValidator()
        validate(external_recipe_href)
        query_string = urlencode({'title' : str(external_recipe_title), 
                        'href' : str(external_recipe_href), 
                        'ing' : str(external_recipe_ing)})
        base_url = '/extrecipe'
        print("---",external_recipe_href,"---",external_recipe_ing, "---")
        url = '{}?{}'.format(base_url, query_string)
        return url            
        
        

    
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
    template_name = "DishDecoderApp/register.html"
    def get(self, req):
        self.form = Create_user_form()
        template_data = {}
        if not req.user.is_authenticated:
            template_data['reg_form']=self.form
            template_data['title_page']='Register'
            return render(req, self.template_name, template_data)
        return redirect('/')

    def post(self, req):
        if not req.user.is_authenticated:
            template_data = {}
            if req.method == 'POST':
                self.form = Create_user_form(req.POST)
                if self.form.is_valid():
                    self.form.save()
                    return redirect('/login/')
                else:
                    template_data['reg_form'] = self.form
                    template_data['title_page'] = 'Register'
                    return render(req, self.template_name,template_data)
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
    template_name="DishDecoderApp/login.html"
    form = AuthenticationForm()
    def get(self, req):
        if not req.user.is_authenticated:
            template_data = {}
            template_data['auth_form']=self.form
            template_data['title_page']='Log in'
            return render(req, self.template_name,template_data)
        return redirect('/')
    
    def post(self, req):
        if not req.user.is_authenticated:
            template_data = {}
            username = req.POST.get('username')
            password = req.POST.get('password')
            user = authenticate(req,username=username,password=password)
            if user is not None:
                login(req,user)
                nextData = req.GET.get('next')
                if(nextData is not None):
                    return redirect(nextData)
                return redirect('/')
            else:
                messages.warning(req,'Login credentials invalid')
                template_data['auth_form']=self.form
                template_data['title_page']='Log in'
                return render(req, self.template_name,template_data)
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
    template_name = "DishDecoderApp/user_profile.html"
    def get(self, req):
        template_data = {}
        if Recipes.objects.filter(author=req.user.id).exists():
            created_data=Recipes.objects.filter(author=req.user.id).all()
            template_data['created_recipes']=created_data
        if Ratings.objects.filter(id_autor=req.user.id).exists():
            rating_data=Ratings.objects.filter(id_autor=req.user.id).all()
            template_data['scored_recipes']=rating_data
        template_data['title_page']='User profile'
        return render(req, self.template_name, template_data)

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
    template_name=""
    form_function=Change_password_form
    title_page=""

    def get(self, req):
        template_data={}
        template_data['change_data_form']=self.form_function(req.user)
        template_data['title_page']=self.title_page
        return render(req, self.template_name, template_data)


    def post(self, req):
        template_data={}
        form = self.form_function(req.user,req.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
        else:
            messages.warning(req,'Invalid data entered')
        return self.get(req)

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
    form = Comments_form()
    template_name="DishDecoderApp/recipe.html" 
    def get(self, req, recipeid):
        template_data={}
        form = Comments_form(req.POST)
        try :
            recipe = Recipes.objects.get(id=recipeid)
            rec_prod = Recipe_Product.objects.filter(id_recipe=recipeid)

            nutrients = Nutrients.objects.all()

            res = self.get_nutritional_value_foreach_nutrition(rec_prod)
            steps = recipe.steps.strip().split('#')
            steps = [x for x in steps if x.strip()]

            rating_data = Ratings.objects.filter(id_recipe=recipeid).all()
            try:
                template_data['average_score'] = sum([recipe_rating.rating for recipe_rating in rating_data]) / rating_data.count()
            except ZeroDivisionError as e:
                pass
            #    average = "Not rated"

            template_data['steps'] = steps
            template_data['recipe'] = recipe
            template_data['rec_prod'] = rec_prod
            template_data['nut_value'] = res
            template_data['rating_data'] = rating_data
            #template_data['average_score'] = average
            template_data['title_page']='Recipe Profile'
            template_data['Comments_form'] = form
            template_data['ratings'] = Ratings
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


    def post(self, req, recipeid):
        if req.user.is_authenticated:
            try:
                recipe = Recipes.objects.get(id=recipeid)
                hasreview=False
                reviewuser=req.user
                if(reviewuser != recipe.author):
                    form = Comments_form(req.POST)
                    desc=req.POST.get('desc')
                    rating=req.POST.get('rating')
                    try:
                        newReview = Ratings.objects.create( id_autor=reviewuser, id_recipe=Recipes.objects.get(id=recipeid),desc=desc,rating=rating)
                        newReview.full_clean()
                        return redirect('/recipe/'+str(recipeid))
                    except ValidationError:
                        newReview.delete()
                        messages.warning(req, 'Invalid rating data')
                        return redirect('/recipe/'+str(recipeid))
                    except IntegrityError:
                        messages.warning(req, 'Only one review per user and recipe')
                        return redirect('/recipe/'+str(recipeid))
                else:
                    messages.warning(req, 'The author of the Recipe is not allowed to add ratings')
                    return redirect('/recipe/'+str(recipeid))
            except Recipes.DoesNotExist:
                return page_not_found(req, exception=None)
        else:
            return redirect('/login/?next=/recipe/'+str(recipeid))


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
    template_name ='DishDecoderApp/createrecipe.html'
    form = Create_recipe_form()
    articleFormSet = formset_factory(Add_products_form)
    def get(self, req):
        return self.returnSharedForm(req)

    def post(self, req):
        recipeuser = req.user
        recipename = req.POST.get('name')
        recipesteps = req.POST.get('steps')
        numberOfForms = req.POST.get('form-TOTAL_FORMS')
        if recipename is not None and recipesteps is not None and numberOfForms is not None:
            try:
                newRecipe = Recipes.objects.create(name=recipename,author=recipeuser,steps=recipesteps)
                numberOfForms = int(numberOfForms)
                if(numberOfForms-1) <= 0:
                    Recipes.objects.filter(id=newRecipe.id).delete()
                    messages.add_message(req, messages.ERROR, 'Incorrect number of ingredients')
                    return self.returnSharedForm(req)
                elif not self.putIngredientsIntoRecipe(newRecipe, req, numberOfForms):
                    Recipes.objects.filter(id=newRecipe.id).delete()
                    return self.returnSharedForm(req)
            except:
                messages.add_message(req, messages.ERROR, 'Incorrect Recipe format')
                return self.returnSharedForm(req)  
        else:
            return self.returnSharedForm(req)
        return redirect("/recipe/"+str(newRecipe.id))

    def putIngredientsIntoRecipe(self, newRecipe, req,numberOfForms):
        for i in range(1,numberOfForms,1):
            product = req.POST.get('form-'+str(i)+'-id_product')
            quantity = req.POST.get('form-'+str(i)+'-quantity')
            if product is not None and quantity is not None and not product=="" and float(quantity)>0:
                try:
                    Recipe_Product.objects.create(id_recipe=newRecipe,id_product=BasicProducts.objects.filter(id=product).first(),quantity=quantity)
                except IntegrityError:
                    messages.add_message(req, messages.ERROR, 'Ingredient already set')
                    return False
                except:
                    messages.add_message(req, messages.ERROR, 'Ingredient quantity too great(0-999)')
                    return False
            else:
                messages.add_message(req, messages.ERROR, 'Incorrect Ingredient format')
                return False
        return True
    
    def returnSharedForm(self, req):
        template_data = {}
        template_data['recipe_basic_form'] = self.form
        template_data['formset'] = self.articleFormSet
        template_data['title_page']='Create_recipe'
        return render(req,self.template_name,template_data)

# Not implemented
#@login_required(login_url='/login/')
#def create_recipe_url(req):
#    return render(req,'DishDecoderApp/createrecipe.html')

class list_recipes_edit_url(LoginRequiredMixin,View):
    login_url = '/login/'
    template_name=""
    baseurl=''
    title_page="Your Recipes"
    def get(self, req):
        template_data = {}
        self.template_name="DishDecoderApp/listeditrecipes.html"
        self.baseurl='/edit/'
        data_fields = Recipes.objects.filter(author=req.user).all()
        if data_fields.count()==1:
            url=self.baseurl+str(getattr(data_fields.first(),'id'))
            return redirect(url)
        template_data["listedtuples"]=data_fields
        template_data['title_page']=self.title_page
        return render(req,self.template_name,template_data)


class edit_recipe_url(LoginRequiredMixin,View):
    login_url = '/login/'
    template_name = "DishDecoderApp/edit_recipe.html"
    baseurl = '/edit/'
    title_page = "Your Recipes"
    form = Create_recipe_form()
    articleFormSet = formset_factory(Add_products_form)

    def get(self, req, recipeid):
        template_data = {}
        recipe_data = Recipes.objects.get(id=recipeid)
        ingredients_data = Recipe_Product.objects.filter(id_recipe=recipeid).all()
        template_data["recipe_data"]=recipe_data
        template_data["ingredients_data"]=ingredients_data
        template_data["recipe_form"]=self.form
        template_data["ingredients_forms"]=self.fill_ingredient_form(recipeid)
        template_data['title_page']=self.title_page
        return render(req,self.template_name,template_data)
    
    def post(self, req, recipeid):
        recipe = Recipes.objects.get(id=recipeid)
        if req.POST.get('name') is not None:
            if not self.change_simple_field(recipe, req, "name"):
                return self.get(req,recipeid)
        elif req.POST.get('steps') is not None:
            if not self.change_simple_field(recipe, req, "steps"):
                return self.get(req,recipeid)
        elif req.POST.get('form-TOTAL_FORMS') is not None:
            if int(req.POST.get('form-TOTAL_FORMS')) > 0:
                if( not self.putIngredientsIntoRecipe(req, recipe, int(req.POST.get('form-TOTAL_FORMS')))):
                    return self.get(req,recipeid)
            else:
                messages.add_message(req, messages.ERROR, 'Incorrect number of ingredients')
                return self.get(req,recipeid)
        return redirect('/recipe/'+str(recipeid))

    def change_simple_field(self,recipe,req,field):
        try:
            if field == "name":
                recipe.name = req.POST.get('name')
            else:
                recipe.steps = req.POST.get('steps')
            recipe.full_clean()
            recipe.save()
        except Exception as e:
            if field == "name":
                messages.add_message(req, messages.ERROR, 'Incorrect name')
            else:
                messages.add_message(req, messages.ERROR, 'Incorrect steps')
            return False
        return True
                
    def putIngredientsIntoRecipe(self, req, editedRecipe, numberOfForms):
        if self.checkValidIngredients(req,numberOfForms):
            Recipe_Product.objects.filter(id_recipe=editedRecipe).delete()
            for i in range(0,numberOfForms,1):
                product = req.POST.get('form-'+str(i)+'-id_product')
                quantity = req.POST.get('form-'+str(i)+'-quantity')
                try:
                    Recipe_Product.objects.create(id_recipe=editedRecipe,id_product=BasicProducts.objects.filter(id=product).first(),quantity=quantity)
                except IntegrityError:
                    messages.add_message(req, messages.ERROR, 'Ingredient already set')
                    return False
                except:
                    messages.add_message(req, messages.ERROR, 'Ingredient quantity too big(0-999)')
                    return False
            return True
        return False

    def checkValidIngredients(self,req, numberOfForms):
        for i in range(0,numberOfForms,1):
            product = req.POST.get('form-'+str(i)+'-id_product')
            quantity = req.POST.get('form-'+str(i)+'-quantity')
            if product is None or quantity is None or product=="" or float(quantity)<=0:
                messages.add_message(req, messages.ERROR, 'Incorrect Ingredient format')
                return False
        return True

    def fill_ingredient_form(self, recipeid):
        data=[]
        ingredients_data = Recipe_Product.objects.filter(id_recipe=recipeid).all()
        for ingredient in ingredients_data:
            data.append({'id_product':ingredient.id_product,'quantity':ingredient.quantity})
        return self.articleFormSet(initial=data)



class erase_recipe_url(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self, req):
        template_data={}
        template_name="DishDecoderApp/listeraserecipes.html"
        title_page="Your Recipes"
        newForm = erase_recipe_form(req.user)
        recipes_count=Recipes.objects.filter(author=req.user).all().count()
        if recipes_count >= 1:
            template_data['form']=newForm
        template_data['title_page']=title_page
        return render(req,template_name,template_data)   

    def post(self, req):
        recipes = dict(req.POST).get('recipes')
        if recipes is not None:
            for recipe in recipes:
                Recipes.objects.filter(id=recipe,author=req.user).delete()
        return redirect("/")


class external_recipe_url(View):
    template_name = "DishDecoderApp/extrecipe.html"
    def get(self, req):
        template_data = {}
        template_data['title'] = req.GET.get('title')
        template_data['ing'] = req.GET.get('inf')
        template_data['href'] = req.GET.get('href')
        return render(req, self.template_name, template_data)

