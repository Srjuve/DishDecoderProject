from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import *
from django.contrib.auth.models import User

use_step_matcher("parse")
@when(u'I fill the comment with "{desc}" with rate "{rating}"')
def step_impl(context, desc, rating):
 
    form = context.browser.find_by_tag('form')

    context.browser.fill('desc', desc)
    context.browser.fill('rating',rating)
@when(u'I click on summit comment button')
def step_impl(context):
    create_btn = context.browser.find_by_id('id_comment')
    create_btn.click()
@then(u'I view the recipe "{id}" with comments by "{user}"')
def step_impl(context,id, user):
    reciperating = context.browser.find_by_id('recipe_rating').text
    #print(context.browser.html)
    assert reciperating == "Rating: 8.00"
    #assert "1"=="2" per a veure el html de la pagina per a la part dels comments dels users
