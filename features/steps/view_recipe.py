from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import recipe_profile_url
from django.contrib.auth.models import User

use_step_matcher("parse")
@given(u'Exists a recipe id "{id}" created by the User "{user}" with "{inunits}" units of the the Ingredient with id "{inid}" that contains "{nutunits}" units of the Nutrient with id "{nutid}"')
def step_impl(context,id,user,inunits,inid,nutunits,nutid):
    createdUser = User.objects.create_user(username=user, email='user@potatoe.com', password='Exemple123')
    recipe = Recipes.objects.create(id=id, name='Recipe1', author=createdUser, steps="#Step1#Step2")
    basicproduct = BasicProducts.objects.create(id=inid,name="Ingredient1",desc="Description1",unit="Gram")
    nutrient = Nutrients.objects.create(id=nutid,name="Nutrient1",desc="Description2")
    Recipe_Product.objects.create(id_recipe=recipe,id_product=basicproduct,quantity=inunits)
    Product_Nutrients.objects.create(id_product=basicproduct,quantity=nutunits,id_nutrient=nutrient)
    

@when(u'I search the recipe id "{id}"')
def step_impl(context,id):
    from DishDecoderApp.models import Recipes
    context.browser.visit(context.get_url("/recipe/"+id))

@then(u'I\'m viewing the details page for the recipe id "{id}"')
def step_impl(context, id):
    #elems = context.browser.find_by_tag('h1')
    #recipeData = Recipes.objects.get(id=id)
    #recipeProductData = Recipe_Product.objects.get(id_recipe=recipeData)
    #basicProductData = recipeData.basic_products.all().first()
    #basicProductIngredientData = Product_Nutrients.objects.get(id_product=basicProductData)
    #nutrientsData = basicProductData.nutrients.all().first()
    check_first_scenario_values(context,id)
    raise NotImplementedError("Patata")


def check_first_scenario_values(context,id):
    recipename = context.browser.find_by_id('recipe_name').text
    assert recipename == Recipes.objects.get(id=id).name
    recipeauthor = context.browser.find_by_id('recipe_author').text
    assert recipeauthor == "by "+Recipes.objects.get(id=id).author.username
    reciperating = context.browser.find_by_id('recipe_rating').text
    assert reciperating == "Rating: Not rated"
    
    recipeingredients = context.browser.find_by_id('recipe_ingredients').find_by_tag('a')
    realingredients = Recipe_Product.objects.filter(id_recipe=id).first()
    for ingredient in recipeingredients:
        assert ingredient.text == str(realingredients.quantity)+str(realingredients.id_product.unit)+" "+str(realingredients.id_product.name)

    stepsdata = context.browser.find_by_id('recipe_steps').find_by_tag('li')
    realsteps = Recipes.objects.get(id=id).steps.split(sep="#")
    i=1
    for step in stepsdata:
        actualStep = step.text.split()[-1]
        assert actualStep == realsteps[i]
        i+=1

    #nutrientsdata = context.browser.find_by_id('recipe_nutrients').find_by_tag('a')
    #for nutrient in nutrientsdata:
    #    nutrientText = nutrient.text
    #    print(nutrientText)

    