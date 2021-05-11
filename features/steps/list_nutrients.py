from behave import *
from DishDecoderApp.models import *
from django.contrib.auth.models import User
from utils import toggle_down_navbar

use_step_matcher("parse")
#test1
@given(u'A nutrient with id "{id}" and a nutrient with id "{id2}"')
def step_impl(context,id,id2):
    Nutrients.objects.create(id=id,name="nutrient1",desc="test2")
    Nutrients.objects.create(id=id2,name="nutrient2",desc="test1")

@when(u'I click nutrients and i search nutrient and i click search')
def step_impl(context):
    context.browser.visit(context.get_url("/"))
    form = context.browser.find_by_tag('form')
    form.find_by_id('id_request_objective_2').first.click()
    context.browser.fill('item_name', "nutrient")
    form.find_by_css('input[name="submit"]').first.click()

@then(u'I\'m seeing a list')
def step_impl(context):
    assert context.browser.is_text_present('nutrient1')
    assert context.browser.is_text_present('nutrient2')

#test2
@when(u'I search for a nutrient that not exist')
def step_impl(context):
    context.browser.visit(context.get_url("/"))
    form = context.browser.find_by_tag('form')
    form.find_by_id('id_request_objective_2').first.click()
    context.browser.fill('item_name', "recipe")
    form.find_by_css('input[name="submit"]').first.click()

@then(u'I\'m seeing an error')
def step_impl(context):
    assert context.browser.is_text_present('No Data Found')