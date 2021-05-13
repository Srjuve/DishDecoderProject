from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")

@given(u'Exists a recipe "{recipe_title}" created by "{recipe_author}"')
def step_impl(context, recipe_title, recipe_author):
    recipe = Recipes.objects.create(name=recipe_title, author=recipe_author, steps="")


@when(u'I click on erase recipe button')
def step_impl(context):
    


@when(u'I select "soup" for deleting purposes')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select "soup" for deleting purposes')


@then(u'Recipe "soup" cannot be found in profile')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Recipe "soup" cannot be found in profile')
