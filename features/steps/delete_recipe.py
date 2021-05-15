from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")

@given(u'Exists a recipe "{recipe_title}" created by "{author_name}"')
def step_impl(context, recipe_title, author_name):
    from DishDecoderApp.models import Recipes
    from django.contrib.auth.models import User
    author = User.objects.filter(username=author_name).first()
    recipe = Recipes.objects.create(name=recipe_title, author=author, steps="Step1")


@when(u'I click on erase recipe button')
def step_impl(context):
    erase_btn = context.browser.find_by_id('erase-btn')
    erase_btn.click()

@when(u'I select "{recipe_title}" for deleting purposes')
def step_impl(context, recipe_title):
    from DishDecoderApp.models import Recipes
    recipe = Recipes.objects.filter(name=recipe_title).first()
    recipe_id = recipe.id
    form = context.browser.find_by_tag('form')
    ul = form.find_by_tag('ul')
    ul.find_by_css('input[value="' + str(recipe_id) + '"]').last.click()
    form.find_by_css('button[type="submit"]').last.click()


@then(u'Recipe "{recipe_title}" cannot be found in profile')
def step_impl(context, recipe_title):
    context.browser.visit(context.get_url("/profile/"))
    assert not context.browser.is_text_present(recipe_title)