from behave import *

from utils import toggle_down_navbar
from DishDecoderApp.models import *

@given(u'Exists a nutrient "{name}" but without description')
def step_impl(context,name):
    Nutrients.objects.create(name=name)

@given(u'Exists a nutrient "{nutrientName}" and the description "{description}"')
def step_impl(context, nutrientName, description):
    Nutrients.objects.create(name=nutrientName, desc=description)

@given(u'Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)

@given(u'Exists the ingredient "{ingredient_name}" with description "{ingredient_desc}"')
def step_impl(context, ingredient_name, ingredient_desc):
    from DishDecoderApp.models import BasicProducts
    BasicProducts.objects.create(name=ingredient_name, desc=ingredient_desc)

@given(u'Exists a recipe "{recipe_title}" created by "{author_name}"')
def step_impl(context, recipe_title, author_name):
    from DishDecoderApp.models import Recipes
    from django.contrib.auth.models import User
    author = User.objects.filter(username=author_name).first()
    recipe = Recipes.objects.create(name=recipe_title, author=author, steps="Step1")

@given(u'Exists the Nutrient "{nutname}" with the description "{description}"')
def step_impl(context, nutname, description):
    Nutrients.objects.create(name=nutname,desc=description)

@given(u'Recipe "{rename}" contains "{quantity}" units of the Ingredient with name "{inname}"')
def step_impl(context,rename,quantity,inname):
    recipe = Recipes.objects.filter(name=rename).first()
    ingredient = BasicProducts.objects.filter(name=inname).first()
    Recipe_Product.objects.create(id_recipe=recipe,id_product=ingredient,quantity=quantity)

@given(u'Ingredient "{inname}" that contains "{quantity}" units of the Nutrient with name "{nutname}"')
def step_impl(context, inname,quantity,nutname):
    ingredient = BasicProducts.objects.filter(name=inname).first()
    nutrient = Nutrients.objects.filter(name=nutname).first()
    Product_Nutrients.objects.create(id_product=ingredient,quantity=quantity,id_nutrient=nutrient)