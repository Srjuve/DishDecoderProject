from behave import *
from DishDecoderApp.models import Nutrients

use_step_matcher("parse")
#Test 1
@given(u'Exists a nutrient id "{id}"')
def step_impl(context,id):
    Nutrients.objects.create(id=id, name='Nutrient1', desc="Nutrient made for the behaviour test")

@when(u'I search the nutrient id "{id}"')
def step_impl(context,id):
    from DishDecoderApp.models import Nutrients
    context.browser.visit(context.get_url("/nutrient/"+id))

@then(u'I\'m viewing the details page for the nutrient id')
def step_impl(context):
    elems = context.browser.find_by_tag('h1')
    assert elems[0].text == "Nutrient1"

#Test 2
@given(u'Exists a nutrient id "{id}" without description')
def step_impl(context,id):
    Nutrients.objects.create(id=id, name='Nutrient2')

@when(u'I search the nutrient id "{id}" without description')
def step_impl(context,id):
    from DishDecoderApp.models import Nutrients
    context.browser.visit(context.get_url("/nutrient/"+id))

@then(u'I\'m viewing the details page for the nutrient without description')
def step_impl(context):
    #assert context.browser.is_text_present == "Nutrient2"
    elems = context.browser.find_by_tag('h1')
    assert elems[0].text == "Nutrient2"
    assert context.browser.is_text_present('No Data Found')

#Test 3
@when(u'I try to search the nutrient id "{id}" which doesn\'t exist')
def step_impl(context,id):
    context.browser.visit(context.get_url("/nutrient/"+id))


@then(u'I\'m expecting to receive an error')
def step_impl(context):   
    assert context.browser.is_text_present('Error 404')
    assert context.browser.is_text_present('The page you are trying to reach does not exist')

