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
urlpatterns = [
    path('',views.main_url, name = "home"),
    path('login/',views.login_page_url, name="login"),
    path('register/',views.register_page_url, name="register"),
    path('logout/',views.logout_url, name="logout"),
    path('recipes/',views.list_recipes_url, name="recipes"),
    path('recipe/<int:recipeid>', views.recipe_profile_url, name="recipe"),
    path('basicproducts/',views.list_basicproducts_url, name="basicproducts"),
    path('basicproduct/<int:basicproductid>',views.basicproduct_profile_url, name="basicproduct"),
    path('nutrients/',views.list_nutrients_url, name="nutrients"),
    path('nutrient/<int:nutrientid>',views.nutrient_profile_url, name="nutrient"),
    path('profile/',views.user_profile_url),
    path('profile/change_password',views.change_password_url, name="changepass"),
    path('profile/change_email',views.change_mail_url, name="changemail"),
    

    path('createrecipe/',views.create_recipe_url, name="createrecipe"),
]