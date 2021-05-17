from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")

@when(u'I write at the autocomplete bar "{recipe_name}"')
def step_impl(context, recipe_name):
    context.browser.visit(context.get_url('/'))
    ac_div = context.browser.find_by_id('autocomplete-div')
    ac_div.find_by_tag('input')[1].fill(recipe_name)

@when(u'I click at submit autocomplete button')
def step_impl(context):
    ac_div = context.browser.find_by_id('autocomplete-div')
    ac_div.find_by_tag('input')[-1].click()

