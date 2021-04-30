from behave import *
from DishDecoderApp.models import Recipes
from django.contrib.auth.models import User

use_step_matcher("parse")
@given(u'Exists a recipe id "{id}" created by the User "{user}"')
def step_impl(context,id,user):
    createdUser = User.objects.create_user(username=user, email='user@potatoe.com', password='Exemple123')
    recipe = Recipes.objects.create(id=id, name='Recipe1', author=createdUser, steps="#Step1#Step2")

@when(u'I search the recipe id "{id}"')
def step_impl(context,id):
    from DishDecoderApp.models import Recipes
    context.browser.visit(context.get_url("/recipe/"+id))

@then(u'I\'m viewing the details page for the recipe id')
def step_impl(context):
    elems = context.browser.find_by_tag('h1')
    assert elems[0].text == "Recipe1"
