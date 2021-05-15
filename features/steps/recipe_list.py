from behave import *
from DishDecoderApp.models import *
from django.contrib.auth.models import User
from utils import toggle_down_navbar

use_step_matcher("parse")
#test1

@given(u'A recipe with id "{id1}" with user "{user1}" and name "{r1}" and a recipe id "{id2}" with user "{user2}" and name "{r2}"')
def step_impl(context,id1,user1,r1,id2,user2,r2):
    cuser1 = User.objects.create_user(username=user1,email='user1@gmail.com',password='Exemple123')
    cuser2 = User.objects.create_user(username=user2,email='user2@gmail.com',password='Exemple1234')
    recipe1 = Recipes.objects.create(id=id1,name=r1 ,author=cuser1,steps='#step1#step2')
    recipe2 = Recipes.objects.create(id=id2,name=r2 ,author=cuser2,steps='#step1#step2')


@when(u'I search for a recipe with name "{recipe}"')
def step_impl(context,recipe):
    context.browser.visit(context.get_url("/"))
    form = context.browser.find_by_tag('form')
    form.find_by_id('id_request_objective_0').first.click()
    context.browser.fill('item_name', recipe)
    form.find_by_css('input[name="submit"]').first.click()

@then(u'I can see the recipe "{recipe_name}"')
def step_impl(context,recipe_name):
    assert context.browser.is_text_present(recipe_name)
