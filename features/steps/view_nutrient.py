from behave import *
from DishDecoderApp.models import Nutrients

use_step_matcher("parse")
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