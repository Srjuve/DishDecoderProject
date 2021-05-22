from behave import *

from utils import toggle_down_navbar
import time
use_step_matcher("parse")

@when(u'I write at the autocomplete bar "{recipe_name}"')
def step_impl(context, recipe_name):
    context.browser.visit(context.get_url('/'))
    context.browser.find_by_id('id_recipe_title').fill(recipe_name)


@when(u'I write at the autocomplete bar "{recipe_name}" and select first option')
def step_impl(context, recipe_name):
    context.browser.visit(context.get_url('/'))
    context.browser.find_by_id('id_recipe_title').fill(recipe_name)
    item_list = context.browser.find_by_id('ui-id-1')
    first_item = item_list.find_by_tag('li')[0]
    first_item.click()

@then(u'I\'m viewing external recipe for "{recipe_name}"')
def step_impl(context, recipe_name):
    assert context.browser.is_text_present(recipe_name)
    assert context.browser.is_text_present("Go to recipe web page")



