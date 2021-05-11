from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import recipe_profile_url
from django.contrib.auth.models import User

use_step_matcher("parse")
    
@given(u'Exists a Ingredient with id "{inid}" that contains "{quantity}" units of the Nutrient ith id "{nutid}"')
def step_impl(context,inid,quantity,nutid):
    basicproduct = BasicProducts.objects.create(id=inid,name="Ingredient2",desc="Description2",unit="Gram")
    nutrient = Nutrients.objects.create(id=nutid,name="Nutrient2",desc="Description2")
    Product_Nutrients.objects.create(id_product=basicproduct,quantity=quantity,id_nutrient=nutrient)
    
@when(u'I click the edit recipe button')
def step_impl(context):
    context.browser.visit(context.get_url('/'))
    edit_btn = context.browser.find_by_id('edit-btn')
    edit_btn.click()

#@when(u'I select the recipe that i am about to edit')
#def step_impl(context):
#    recipe_button = context.browser.find_by_tag('a')
#    recipe_button.click()

@when(u'I fill the recipe name form with the new name "{newname}"')
def step_impl(context,newname):
    input_data = context.browser.find_by_id('nameEditForm').find_by_tag('form')
    context.browser.fill('name',newname)

@when(u'I click the button to change the name')
def step_impl(context):
    change_name_btn = context.browser.find_by_id('name_change_btn')
    change_name_btn.click()

@then(u'I can see that the recipe has the name "{newname}"')
def step_impl(context,newname):
    recipename = context.browser.find_by_id('recipe_name').text
    assert recipename == newname

@when(u'I fill the steps form with the steps "{steps}"')
def step_impl(context,steps):
    input_data = context.browser.find_by_id('stepEditForm').find_by_tag('form')
    context.browser.fill('steps',steps)

@when(u'I click the button to change the steps')
def step_impl(context):
    change_steps_btn = context.browser.find_by_id('steps_change_btn')
    change_steps_btn.click()

@then(u'I can see that the steps are "{steps}"')
def step_impl(context, steps):
    stepsdata = context.browser.find_by_id('recipe_steps').find_by_tag('li')
    realsteps = steps.split(sep="#")
    i=0
    for step in stepsdata:
        actualStep = step.text.split()[-1]
        assert actualStep == realsteps[i]
        i+=1

@when(u'I add "{quantity}" units of the Ingredient with id "{inid}"')
def step_impl(context,quantity,inid):
    input_data = context.browser.find_by_id('id_form-1-quantity')
    select_data = context.browser.find_by_id('id_form-1-id_product')
    select_data.select(inid)
    input_data.fill(quantity)

@when(u'I click the button to add the Ingredients')
def step_impl(context):
    change_ing_btn = context.browser.find_by_id('ing_change_btn')
    change_ing_btn.click()

@then(u'I can see the Ingredients data')
def step_impl(context):
    pass

def check_ingredients(context,id):
    recipeingredients = context.browser.find_by_id('recipe_ingredients').find_by_tag('a')
    realingredients = Recipe_Product.objects.filter(id_recipe=id).first()
    for ingredient in recipeingredients:
        assert ingredient.text == str(round(realingredients.quantity,2))+str(realingredients.id_product.unit)+" "+str(realingredients.id_product.name)

def check_nutrients(context, id):
    product_nutrients_data = get_nutritional_value_foreach_nutrition(Recipe_Product.objects.filter(id_recipe=id))
    nutrientsdata = context.browser.find_by_id('recipe_nutrients').find_by_tag('a')
    i=0
    for nutrient in nutrientsdata:
        actualValue = str(round(product_nutrients_data[i][0],2))+"g "+product_nutrients_data[i][1].name
        assert nutrient.text == actualValue
        i+=1

@given(u'I am on main page')
def step_impl(context):
    context.browser.visit(context.get_url('/'))