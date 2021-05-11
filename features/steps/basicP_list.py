from typing import ByteString
from behave import *
from DishDecoderApp.models import *
from django.contrib.auth.models import User
from utils import toggle_down_navbar


use_step_matcher("parse")
#test1
@given(u'A BasicProduct with id "{id}" and a BasicProduct id "{id2}"')
def step_impl(context,id,id2):
    BasicProducts.objects.create(id=id,name="ingredient1",desc="desc",unit="gram")
    BasicProducts.objects.create(id=id2,name="ingredient2",desc="desc2",unit="grams")

@when(u'I click BasicProducts and i search products and i click search')
def step_impl(context):
    context.browser.visit(context.get_url("/"))
    form = context.browser.find_by_tag('form')
    form.find_by_id('id_request_objective_1').first.click()
    context.browser.fill('item_name', "ingredient")
    form.find_by_css('input[name="submit"]').first.click()

@then(u'I see ingredients')
def step_impl(context):
    assert context.browser.is_text_present('ingredient1')
    assert context.browser.is_text_present('ingredient2')
#test2
@when(u'I search for a basic product that not exist')
def step_impl(context):
    context.browser.visit(context.get_url("/"))
    form = context.browser.find_by_tag('form')
    form.find_by_id('id_request_objective_1').first.click()
    context.browser.fill('item_name', "ingredient")
    form.find_by_css('input[name="submit"]').first.click()

@then(u'An error appears')
def step_impl(context):
    assert context.browser.is_text_present('No Data Found')