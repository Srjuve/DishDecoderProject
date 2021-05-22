from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import *
from django.contrib.auth.models import User


use_step_matcher("parse")     

@then(u'I\'m viewing the details page of basic product "{bpname}" with description "{bpdesc}"')
def step_impl(context, bpname, bpdesc):
    print(context.browser.html)
    desciption1 = context.browser.find_by_id('description').text
    assert desciption1 == bpdesc
    ingredientname = context.browser.find_by_id('basic_product_name').text
    assert ingredientname == bpname

@then(u'This basic product details page shows the recipe "{rname}"')
def step_impl(context, rname):
    recipename = context.browser.find_by_id('recipes').find_by_tag('a').first.text
    assert recipename == rname

