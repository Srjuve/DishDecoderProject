from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import recipe_profile_url
from django.contrib.auth.models import User

use_step_matcher("parse")
@given(u'Exists a recipe id "{id}" created by the User "{user}" with "{inunits}" units of the the Ingredient with id "{inid}" that contains "{nutunits}" units of the Nutrient with id "{nutid}"')
def step_impl(context,id,user,inunits,inid,nutunits,nutid):
    createdUser = User.objects.get(username=user)
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
        assert ingredient.text == str(realingredients.quantity)+str(realingredients.id_product.unit)+" "+str(realingredients.id_product.name)



def check_steps(context, id):
    stepsdata = context.browser.find_by_id('recipe_steps').find_by_tag('li')
    realsteps = Recipes.objects.get(id=id).steps.split(sep="#")

    i=1
    for step in stepsdata:
        actualStep = step.text.split()[-1]
        assert actualStep == realsteps[i]
        i+=1

def check_nutrients(context, id):
    product_nutrients_data = get_nutritional_value_foreach_nutrition(Recipe_Product.objects.filter(id_recipe=id))
    nutrientsdata = context.browser.find_by_id('recipe_nutrients').find_by_tag('a')
    i=0
    for nutrient in nutrientsdata:
        actualValue = str(product_nutrients_data[i][0])+"g "+product_nutrients_data[i][1].name
        assert nutrient.text == actualValue
        i+=1

def get_nutritional_value_foreach_nutrition(rec_prod):
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

    