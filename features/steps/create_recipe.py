from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")

@given(u'Exists the ingredient "{ingredient_name}"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Exists the ingredient "meat"')


@then(u'pepito')
def step_impl(context):
    print(context.browser.html)

@when(u'I click on create recipe button')
def step_impl(context):
    create_btn = context.browser.find_by_id('create-btn')
    create_btn.click()

@when(u'I fill the name of the recipe "{recipe_name}"')
def step_impl(context, recipe_name):
    form = context.browser.find_by_tag('form')
    context.browser.fill('name', recipe_name)


@when(u'I fill the steps of the recipe "{recipe_steps}"')
def step_impl(context, recipe_steps):
    form = context.browser.find_by_tag('form')
    context.browser.fill('steps', recipe_steps)

@when(u'I add the ingredient "{ingredient_name}" with quantity "{ingredient_quantity}"')
def step_impl(context, ingredient_name, ingredient_quantity):
    #De 3 fins len - 4
    add_ing = context.browser.find_by_id('add_form')
    add_ing.click()
    inputs = context.browser.find_by_tag('input')[3:-4]
    options = context.browser.find_by_tag('option')
    for e in inputs:
        print("->", e['id'])
    for e in options:
        print("oo>", e['id'])
    print(len(inputs))
    ing_name = options[-1]
    ing_quant = inputs[-1]
    ing_name.select(ingredient_name)
    ing_quant.fill(ingredient_quantity)

@when(u'I finish recipe')
def step_impl(context):
    context.browser.find_by_css('button[type="submit"]').last.click()



@then(u'I click on profile button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I click on profile button')


@then(u'I click on recipe with name "{recipe_name}"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I click on recipe with name "Paella"')


@then(u'I can see recipe name "{recipe_name}"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can see recipe name "Paella"')


@then(u'I can see recipe steps "#Lorem#Ipsum#Dolor#Sit#Amet"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can see recipe steps "#Lorem#Ipsum#Dolor#Sit#Amet"')


@then(u'I can see recipe ingredient "{ingredient_name}" with quantity "{ingredient_quantity}"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can see recipe ingredient "rice" with quantity "250"')

