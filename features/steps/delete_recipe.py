from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")


@when(u'I select "{recipe_title}" for deleting purposes')
def step_impl(context, recipe_title):
    from DishDecoderApp.models import Recipes
    recipe = Recipes.objects.filter(name=recipe_title).first()
    recipe_id = recipe.id
    form = context.browser.find_by_tag('form')
    assert context.browser.is_element_present_by_tag('ul', wait_time=5)
    ul = form.find_by_tag('ul')
    ul.find_by_css('input[value="' + str(recipe_id) + '"]').last.click()
    form.find_by_css('button[type="submit"]').last.click()


@then(u'Recipe "{recipe_title}" cannot be found in profile')
def step_impl(context, recipe_title):
    context.browser.visit(context.get_url("/profile/"))
    assert not context.browser.is_text_present(recipe_title)