from behave import *
from DishDecoderApp.models import Nutrients

use_step_matcher("parse")
#Test 1
@given(u'Exists a nutrient id "{id}" with the name "{nutrientName}" and the description "{description}"')
def step_impl(context,id, nutrientName, description):
    Nutrients.objects.create(id=id, name=nutrientName, desc=description)

@when(u'I search the nutrient id "{id}"')
def step_impl(context,id):
    from DishDecoderApp.models import Nutrients
    context.browser.visit(context.get_url("/nutrient/"+id))

@then(u'I\'m viewing the page for the nutrient "{nutrientName}"')
def step_impl(context,nutrientName):
    elems = context.browser.find_by_tag('h1')
    assert elems[0].text == nutrientName

@then(u'I can also see the description "{description}"')
def step_impl(context,description):
    assert context.browser.is_text_present(description)

#Test 2
@given(u'Exists a nutrient id "{id}" with the name "{name}" but without description')
def step_impl(context,id,name):
    Nutrients.objects.create(id=id, name=name)

@then(u'I can see that there\'s no description')
def step_impl(context):
    assert context.browser.is_text_present('No Data Found')

#Test 3
@when(u'I try to search the nutrient id "{id}" which doesn\'t exist')
def step_impl(context,id):
    context.browser.visit(context.get_url("/nutrient/"+id))


@then(u'I\'m expecting to receive an error')
def step_impl(context):   
    assert context.browser.is_text_present('Error 404')
    assert context.browser.is_text_present('The page you are trying to reach does not exist')

