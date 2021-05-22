from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import recipe_profile_url
from django.contrib.auth.models import User

use_step_matcher("parse")
        

@when(u'I fill the recipe name form with the new name "{newname}"')
def step_impl(context,newname):
    input_data = context.browser.find_by_id('nameEditForm').find_by_tag('form')
    context.browser.fill('name',newname)

@when(u'I click the button to change the name')
def step_impl(context):
    change_name_btn = context.browser.find_by_id('name_change_btn')
    change_name_btn.click()

@when(u'I fill the steps form with the steps "{steps}"')
def step_impl(context,steps):
    input_data = context.browser.find_by_id('stepEditForm').find_by_tag('form')
    context.browser.fill('steps',steps)

@when(u'I click the button to change the steps')
def step_impl(context):
    change_steps_btn = context.browser.find_by_id('steps_change_btn')
    change_steps_btn.click()

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

    
@when(u'I click the button to erase Ingredients')
def step_impl(context):
    erase_btn = context.browser.find_by_id('erase_form')
    erase_btn.click()
