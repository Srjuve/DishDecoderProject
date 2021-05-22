from behave import *
from DishDecoderApp.models import Nutrients

use_step_matcher("parse")

@then(u'I view the page for the nutrient "{nutrientName}"')
def step_impl(context,nutrientName):
    elems = context.browser.find_by_tag('h1')
    assert elems[0].text == nutrientName

@then(u'I can also see the description "{description}"')
def step_impl(context,description):
    assert context.browser.is_text_present(description)


