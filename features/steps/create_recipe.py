from behave import *

from utils import toggle_down_navbar, get_nutritional_value_foreach_nutrition

from DishDecoderApp.models import Recipe_Product

use_step_matcher("parse")

@given(u'Exists the ingredient "{ingredient_name}" with description "{ingredient_desc}"')
def step_impl(context, ingredient_name, ingredient_desc):
    from DishDecoderApp.models import BasicProducts
    BasicProducts.objects.create(name=ingredient_name, desc=ingredient_desc)

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
    #print(list(context.browser.find_by_tag('input')), list(context.browser.find_by_tag('option')))
    #for e in inputs:
    #    print("-->", e['id'], "<--")
    #for e in options:
    #    print("oo>", e['selected'], e['text'], "<oo")
    #for e in selects:
    #    print("oo>", e['id'], "<oo")
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
        ing_name = item.text.split()[1]
        if ing_name == ingredient_name:
            ing_quant = ingredient_quantity + " " + ingredient_name
            assert ing_quant == item.text
            break

@then(u'I stay at "{current_url}"')
def step_impl(context, current_url):
    assert context.browser.url.replace(context.get_url('/'), '/') == current_url


@then(u'I can see recipe nutrient "{nutrient_name}" with quantity "{nutrient_quantity}"')
def step_impl(context, nutrient_name, nutrient_quantity):
    nut_cont = context.browser.find_by_id("recipe_nutrients")
    nut_items = nut_cont.find_by_tag("a")
    nut_item = None
    for item in nut_items:
        nut_name = item.text.split()[1]
        if nut_name == nutrient_name:
            nut_item = item
    if nut_item:
        recipe_id = context.browser.url.split("/")[-1]
        nut_vals = get_nutritional_value_foreach_nutrition(Recipe_Product.objects.filter(id_recipe=recipe_id))
        for nut_val in nut_vals:
            if nut_val[1].name == nutrient_name:
                actual_val = str(round(nut_val[0],2))+"g "+nut_val[1].name
                expected_val = nutrient_quantity + " " + nutrient_name
                assert actual_val, expected_val

    else:
        raise ValueError("{nutrient_name} not found in page")