from behave import *
from DishDecoderApp.models import *
from django.contrib.auth.models import User
from utils import toggle_down_navbar

use_step_matcher("parse")
#test1
@given(u'A nutrient with id "{id}" and name "{name1}" a nutrient with id "{id2}" with name "{name2}"')
def step_impl(context,id,name1,id2,name2):
    Nutrients.objects.create(id=id,name=name1,desc="test2")
    Nutrients.objects.create(id=id2,name=name2,desc="test1")

@when(u'I click nutrients and i search "{word}" and i click search')
def step_impl(context,word):
    context.browser.visit(context.get_url("/"))
    form = context.browser.find_by_tag('form')
    form.find_by_id('id_request_objective_2').first.click()
    context.browser.fill('item_name', word)
    form.find_by_css('input[name="submit"]').first.click()

@then(u'I\'m seeing the nutrients "{name1}" and "{name2}"')
def step_impl(context,name1,name2):
    assert context.browser.is_text_present(name1)
    assert context.browser.is_text_present(name2)

#test2
@when(u'I search for "{name}"')
def step_impl(context,name):
    context.browser.visit(context.get_url("/"))
    form = context.browser.find_by_tag('form')
    form.find_by_id('id_request_objective_2').first.click()
    context.browser.fill('item_name', name)
    form.find_by_css('input[name="submit"]').first.click()

@then(u'I\'m seeing an error')
def step_impl(context):
    assert context.browser.is_text_present('No Data Found')