from behave import *
from DishDecoderApp.models import Nutrients

use_step_matcher("parse")
#Test 1
@when(u'I search the nutrient "{name}"')
def step_impl(context,name):
    from DishDecoderApp.models import Nutrients
    nutrientSearched = Nutrients.objects.get(name = name)
    context.browser.visit(context.get_url("/nutrient/"+str(nutrientSearched.id)))

@then(u'I view the page for the nutrient "{nutrientName}"')
def step_impl(context,nutrientName):
    elems = context.browser.find_by_tag('h1')
    assert elems[0].text == nutrientName

@then(u'I can also see the description "{description}"')
def step_impl(context,description):
    assert context.browser.is_text_present(description)

#Test 2
@given(u'Exists a nutrient "{name}" but without description')
def step_impl(context,name):
    Nutrients.objects.create(name=name)

@then(u'I can see that there\'s no description')
def step_impl(context):
    assert context.browser.is_text_present('No Data Found')

#Test 3
@when(u'I search the nutrient id "{id}"')
def step_impl(context,id):
    context.browser.visit(context.get_url("/nutrient/"+id))


@then(u'I receive the error 404')
def step_impl(context):   
    assert context.browser.is_text_present('Error 404')
    assert context.browser.is_text_present('The page you are trying to reach does not exist')

