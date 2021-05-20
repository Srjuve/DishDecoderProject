from behave import *
from DishDecoderApp.models import *
from django.contrib.auth.models import User
from utils import toggle_down_navbar

use_step_matcher("parse")
#test1

@when(u'I search for a recipe with name "{recipe}"')
def step_impl(context,recipe):
    context.browser.visit(context.get_url("/"))
    form = context.browser.find_by_tag('form')
    form.find_by_id('id_request_objective_0').first.click()
    context.browser.fill('item_name', recipe)
    form.find_by_css('input[name="submit"]').first.click()

@then(u'I can see the recipe "{recipe_name}"')
def step_impl(context,recipe_name):
    assert context.browser.is_text_present(recipe_name)
