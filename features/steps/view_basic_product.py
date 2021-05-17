from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import *
from django.contrib.auth.models import User

#test1
use_step_matcher("parse")
@given(u'Exists a basic product with id "{id}" that appears in the recipe with id "{idr}"')
def step_impl(context,id,idr):
    basicproduct = BasicProducts.objects.create(id=id,name="Ingredient1",desc="desciption1",unit="Gram")
    createduser= User.objects.create_user(username="user1",email="user@patata.com",password="Exemple123")
    recipe = Recipes.objects.create(id=idr,name="Recipe1",author=createduser,steps="#step1#step2")
    Recipe_Product.objects.create(id_recipe=recipe,id_product=basicproduct,quantity=1)
    
@when(u'I search the basic product "{id}"')
def step_impl(context,id):
    from DishDecoderApp.models import BasicProducts
    context.browser.visit(context.get_url("/basicproduct/"+id))

@then(u'I\'m viewing the details page for the basic product id "{id}" and appears the recipe with id "{idr}"')
def step_impl(context,id,idr):
    desciption1 = context.browser.find_by_id('description').text
    assert desciption1 == BasicProducts.objects.get(id=id).desc
    ingredientname = context.browser.find_by_id('basic_product_name').text
    assert ingredientname == BasicProducts.objects.get(id=id).name
    recipename = context.browser.find_by_id('recipes').find_by_tag('a').text
    assert recipename == Recipes.objects.get(id=idr).name

#test2
@given(u'Exists a basic product with id "{id}" without recipe')
def step_impl(context,id):
    BasicProducts.objects.create(id=id,name="Ingredient2",desc="desciption2",unit="Gram")

@when(u'I search the basic product with id "{id}" without recipe')
def step_impl(context,id):
    from DishDecoderApp.models import BasicProducts
    context.browser.visit(context.get_url("/basicproduct/"+id))

@then(u'I\'m viewing the details page for the basic product with id "{2}" without recipe')
def step_impl(context,id):
    desciption1 = context.browser.find_by_id('description').text
    assert desciption1 == BasicProducts.objects.get(id=id).desc
    ingredientname = context.browser.find_by_id('basic_product_name').text
    assert ingredientname == BasicProducts.objects.get(id=id).name
    assert context.browser.is_text_present('No Data Found')

#test3
@when(u'I try to search the basic product with id "{id}" which doesn\'t exist')
def step_impl(context,id):
    from DishDecoderApp.models import BasicProducts
    context.browser.visit(context.get_url("/basicproduct/"+id))
