from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")

@given(u'Exists a recipe "{recipe_title}" created by "{author_name}"')
def step_impl(context, recipe_title, author_name):
    from DishDecoderApp.models import Recipes
    from django.contrib.auth.models import User
    author = User.objects.filter(username=author_name).first()
    recipe = Recipes.objects.create(name=recipe_title, author=author, steps="")


@when(u'I click on erase recipe button')
def step_impl(context):
    raise NotImplementedError(u'STEP: I click on erase recipe button')    


@when(u'I select "soup" for deleting purposes')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select "soup" for deleting purposes')


@then(u'Recipe "soup" cannot be found in profile')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Recipe "soup" cannot be found in profile')
