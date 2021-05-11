from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")

@given(u'Exists the ingredient "{ingredient_name}"')
def step_impl(context, ingredient_name):
    from DishDecoderApp.models import BasicProducts
    BasicProducts.objects.create(name=ingredient_name, desc=ingredient_name+", LoremIpsum")

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
    selects = context.browser.find_by_tag('select')
    print(list(context.browser.find_by_tag('input')), list(context.browser.find_by_tag('option')))
    for e in inputs:
        print("-->", e['id'], "<--")
    for e in options:
        print("oo>", e['selected'], e['text'], "<oo")
    for e in selects:
        print("oo>", e['id'], "<oo")
    ing_val = ""
    for option in selects[-1].find_by_tag('option'):
        if ingredient_name == option['text']:
            ing_val = option['value']
    #ing_name = selects[-1]
    ing_quant = inputs[-1]
    ing_quant.fill(ingredient_quantity)
    selects[-1].select(ing_val)

@when(u'I finish recipe')
def step_impl(context):
    context.browser.find_by_css('button[type="submit"]').last.click()

@then(u'I can see recipe name "{recipe_name}" with author username "{username}"')
def step_impl(context, recipe_name, username):
    assert context.browser.is_text_present(recipe_name)
    assert context.browser.is_text_present("by "+username)

@then(u'I can see recipe steps "{recipe_steps}"')
def step_impl(context, recipe_steps):
    steps = recipe_steps.split("#")
    for step in steps:
        assert context.browser.is_text_present(step)

@then(u'I can see recipe ingredient "{ingredient_name}" with quantity "{ingredient_quantity}"')
def step_impl(context, ingredient_name, ingredient_quantity):
    ing_cont = context.browser.find_by_id("ingredient-container")
    ing_item = ing_cont.find_by_tag("a")
    for item in ing_item:
        ing_name = item.text[-1]
        if ing_name == ingredient_name:
            ing_quant = ingredient_quantity + " " + ingredient_name
            assert ing_quant == item.text
            break


@then(u'I stay at "{current_url}"')
def step_impl(context, current_url):
    print("---",context.browser.url.replace(context.get_url('/'), '/'),"---",current_url,"---")
    assert context.browser.url.replace(context.get_url('/'), '/') == current_url

@given(u'I am on main page')
def step_impl(context):
    context.browser.visit(context.get_url('/'))