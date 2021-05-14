from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import recipe_profile_url
from django.contrib.auth.models import User

use_step_matcher("parse")
    
@given(u'Exists a Ingredient with id "{inid}" and name "{inname}" and type "{intype}" that contains "{quantity}" units of the Nutrient with id "{nutid}"')
def step_impl(context,inid,inname,intype,quantity,nutid):
    basicproduct = BasicProducts.objects.create(id=inid,name=inname,desc="Description2",unit=intype)
    nutrient = Nutrients.objects.create(id=nutid,name="Nutrient2",desc="Description2")
    Product_Nutrients.objects.create(id_product=basicproduct,quantity=quantity,id_nutrient=nutrient)
    
@when(u'I click the edit recipe button')
def step_impl(context):
    context.browser.visit(context.get_url('/'))
    edit_btn = context.browser.find_by_id('edit-btn')
    edit_btn.click()

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


@when(u'I add "{quantity}" units of the Ingredient with name "{inname}"')
def step_impl(context,quantity,inname):
    input_data = context.browser.find_by_id('id_form-1-quantity')
    select_data = context.browser.find_by_id('id_form-1-id_product')
    options = select_data.find_by_tag('option')
    ing_val = ""
    for option in options:
        if inname == option['text']:
            ing_val = option['value']
    select_data.select(ing_val)
    input_data.fill(quantity)

@when(u'I click the button to add the Ingredients')
def step_impl(context):
    change_ing_btn = context.browser.find_by_id('ing_change_btn')
    change_ing_btn.click()

@then(u'I can see the Ingredient with id "{inid}" and with name "{inname}" and type "{intype}" with "{quantity}" units')
def step_impl(context,inid,inname,intype,quantity):
    check_ingredients(context, inid, inname,intype, quantity)

def check_ingredients(context,id,inname,intype, quantity):
    ingredient = context.browser.find_by_id('recipe_ingredients').find_by_tag('a').last
    assert ingredient.text == quantity+intype+" "+inname

def check_nutrients(context, id):
    product_nutrients_data = get_nutritional_value_foreach_nutrition(Recipe_Product.objects.filter(id_recipe=id))
    nutrientsdata = context.browser.find_by_id('recipe_nutrients').find_by_tag('a')
    i=0
    for nutrient in nutrientsdata:
        actualValue = str(round(product_nutrients_data[i][0],2))+"g "+product_nutrients_data[i][1].name
        assert nutrient.text == actualValue
        i+=1

@then(u'I see the repeated ingredient error')
def step_impl(context):
    error_message = context.browser.find_by_id('error_messages').find_by_tag('li')
    assert error_message.text == "Ingredient already set"
    
@then(u'I see the invalid ingredient format error')
def step_impl(context):
    error_message = context.browser.find_by_id('error_messages').find_by_tag('li')
    assert error_message.text == "Incorrect Ingredient format"

@then(u'I see the quantity value too big error')
def step_impl(context):
    error_message = context.browser.find_by_id('error_messages').find_by_tag('li')
    assert error_message.text == "Ingredient quantity too big(0-999)"


@when(u'I click the button to erase Ingredients')
def step_impl(context):
    erase_btn = context.browser.find_by_id('erase_form')
    erase_btn.click()

@given(u'In the Recipe with id "{id}" contains the Ingredient with id "{inid}" and name "{inname}" and type "{intype}" that contains "{quantity}" units of the Nutrient with id "{nutid}"')
def step_impl(context,id,inid,inname,intype,quantity,nutid):
    recipe = Recipes.objects.get(id=id)
    basicproduct = BasicProducts.objects.get(id=inid)
    Recipe_Product.objects.create(id_recipe=recipe,id_product=basicproduct,quantity=quantity)


@then(u'I see the incorrect number of Ingredients exceptions')
def step_impl(context):
    error_message = context.browser.find_by_id('error_messages').find_by_tag('li')
    assert error_message.text == "Incorrect number of ingredients"

@then(u'I see that the only ingredient shown is the ingredient with id "{inid}",name "{inname}",type "{intype}" and quantity "{quantity}"')
def step_impl(context,inid,inname,intype,quantity):
    ingredients = context.browser.find_by_id('recipe_ingredients').find_by_tag('a')
    for ingredient in ingredients:
        assert ingredient.text == quantity+intype+" "+inname

@given(u'I am on main page')
def step_impl(context):
    context.browser.visit(context.get_url('/'))