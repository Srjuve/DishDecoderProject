"""DishDecoderProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from DishDecoderApp import views
from django.contrib.auth.decorators import login_required
from DishDecoderApp.models import *
from .forms import Main_page_form, Create_user_form, Change_password_form , Change_email_form
from DishDecoderApp.views import *
urlpatterns = [
    path('',main_url.as_view(), name = "home"),
    path('login/',login_page_url.as_view(), name="login"),
    path('register/',register_page_url.as_view(), name="register"),
    path('logout/',logout_url.as_view(), name="logout"),
    path('recipes/',list_data_url.as_view(template_name="DishDecoderApp/recipes.html",baseurl="/recipe/", searchedObject=Recipes,title_page="Recipes"), name="recipes"),
    path('recipe/<int:recipeid>', recipe_profile_url.as_view(), name="recipe"),
    path('basicproducts/',list_data_url.as_view(template_name="DishDecoderApp/basicproducts.html",baseurl="/basicproduct/", searchedObject=BasicProducts,title_page="Basic Products"), name="basicproducts"),
    path('basicproduct/<int:basicproductid>',basicproduct_profile_url.as_view(), name="basicproduct"),
    path('nutrients/',list_data_url.as_view(template_name="DishDecoderApp/nutrients.html",baseurl="/nutrient/", searchedObject=Nutrients,title_page="Nutrients"), name="nutrients"),
    path('nutrient/<int:nutrientid>',nutrient_profile_url.as_view(), name="nutrient"),
    path('profile/',user_profile_url.as_view()),
    path('profile/change_password',change_data_url.as_view(template_name="DishDecoderApp/change_password.html",form_function=Change_password_form,title_page="Change password"), name="changepass"),
    path('profile/change_email',change_data_url.as_view(template_name="DishDecoderApp/change_email.html",form_function=Change_email_form,title_page="Change email"), name="changemail"),
    #path('autocomplete/', autocomplete_test_url.as_view(), name='autocomplete_test'),
    path('extrecipe/', external_recipe_url.as_view(), name='extrecipe'),
    path('createrecipe/',create_recipe_url.as_view(), name="createrecipe"),
    path('listedit/',list_recipes_edit_url.as_view(), name="listeditrecipe"),
    path('edit/<int:recipeid>',edit_recipe_url.as_view(), name="edit"),
    path('erase/',erase_recipe_url.as_view(),name="listeraserecipe"),
    #path('erase/<int:recipeid>',erase_recipe_url.as_view(),name="erase"),
]
