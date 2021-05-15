from behave import *
from DishDecoderApp.models import *
from django.contrib.auth.models import User
from utils import toggle_down_navbar

use_step_matcher("parse")

@given(u'Exists a nutrient with name "{nut_name}"')
def step_impl(context, nut_name):
    Nutrients.objects.create(name=nut_name,desc=nut_name+", Lorem Ipsum")

@then(u'I can see the nutrient "{nut_name}"')
def step_impl(context, nut_name):
    assert context.browser.is_text_present(nut_name)

@when(u'I search for a nutrient with name "{nut_name}"')
def step_impl(context, nut_name):
    context.browser.visit(context.get_url("/"))
    form = context.browser.find_by_tag('form')
    form.find_by_id('id_request_objective_2').first.click()
    context.browser.fill('item_name', nut_name)
    form.find_by_css('input[name="submit"]').first.click()