from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import recipe_profile_url
from django.contrib.auth.models import User
from utils import get_nutritional_value_foreach_nutrition

use_step_matcher("parse")
    
@given(u'Exists the Nutrient "{nutname}"')
def step_impl(context,nutname):
    Nutrients.objects.create(name=nutname,desc="Description2")


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

@when(u'I search the recipe with name "{rename}"')
def step_impl(context,rename):
    from DishDecoderApp.models import Recipes
    context.browser.visit(context.get_url("/recipe/"+str(Recipes.objects.filter(name=rename).first().id)))

@when(u'I search a recipe with a non existent id')
def step_impl(context):
    from DishDecoderApp.models import Recipes
    context.browser.visit(context.get_url("/recipe/1234567"))

@then(u'I\'m viewing the details page for the recipe with name "{rename}" without the comments')
def step_impl(context, rename):
    id = Recipes.objects.filter(name=rename).first().id
    check_first_scenario_values(context,id)
    check_ingredients(context,id)
    check_steps(context,id)
    check_nutrients(context,id)

@then(u'I\'m viewing the 404 error page')
def step_impl(context):
    title = context.browser.find_by_tag('h1')
    assert title.text == "Error 404"

def check_first_scenario_values(context,id):
    recipename = context.browser.find_by_id('recipe_name').text
    assert recipename == Recipes.objects.get(id=id).name
    recipeauthor = context.browser.find_by_id('recipe_author').text
    assert recipeauthor == "by "+Recipes.objects.get(id=id).author.username
    reciperating = context.browser.find_by_id('recipe_rating').text
    assert reciperating == "Rating: Not rated"
    

def check_ingredients(context,id):
    recipeingredients = context.browser.find_by_id('recipe_ingredients').find_by_tag('a')
    realingredients = Recipe_Product.objects.filter(id_recipe=id).first()
    for ingredient in recipeingredients:
        assert ingredient.text == str(round(realingredients.quantity,2))+str(realingredients.id_product.unit)+" "+str(realingredients.id_product.name)



def check_steps(context, id):
    stepsdata = context.browser.find_by_id('recipe_steps').find_by_tag('li')
    realsteps = Recipes.objects.get(id=id).steps.strip().split(sep="#")
    realsteps = [x for x in realsteps if x.strip()]
    i=0
    for step in stepsdata:
        actualStep = step.text.split()[-1]
        assert actualStep == realsteps[i]
        i+=1

def check_nutrients(context, id):
    product_nutrients_data = get_nutritional_value_foreach_nutrition(Recipe_Product.objects.filter(id_recipe=id))
    nutrientsdata = context.browser.find_by_id('recipe_nutrients').find_by_tag('a')
    i=0
    for nutrient in nutrientsdata:
        actualValue = str(round(product_nutrients_data[i][0],2))+"g "+product_nutrients_data[i][1].name
        assert nutrient.text == actualValue
        i+=1

    