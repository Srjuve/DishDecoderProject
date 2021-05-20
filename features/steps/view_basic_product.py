from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import *
from django.contrib.auth.models import User


use_step_matcher("parse")     
@when(u'I search the basic product with name "{bpname}"')
def step_impl(context,bpname):
    from DishDecoderApp.models import BasicProducts
    context.browser.visit(context.get_url("/basicproduct/"+str(BasicProducts.objects.filter(name=bpname).first().id)))

@when(u'I search the basic product with id "{bpid}"')
def step_impl(context,bpid):
    context.browser.visit(context.get_url("/basicproduct/"+bpid))

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

@then(u'This basic product details page shows no recipe')
def step_impl(context):
    assert context.browser.is_text_present('No Data Found')