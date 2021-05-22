from behave import *
from django.contrib.auth.models import User
from DishDecoderApp.models import Ratings, Recipes

use_step_matcher("parse")

@then(u'I, as the user "{user}", see my profile\'s information.')
def step_impl(context, user):
    assert context.browser.is_text_present('User Profile')
    foundh1 = context.browser.find_by_tag('h1')
    assert foundh1[1]
    assert foundh1[1].text == user

@then (u'I see in my profile that I made the recipe "{recipe}"')
def step_impl(context,recipe):
    assert context.browser.is_text_present('User Profile')
    assert context.browser.is_text_present(recipe)
    

@given (u'I, the user "{user}", made a rating "{rating}" on the recipe "{recipe}"')
def step_impl(context,user, rating,recipe):
    user_data = User.objects.get(username=user)
    chefUser_data = Recipes.objects.get(name=recipe)
    Ratings.objects.create(id_autor = User.objects.get(id=user_data.id),id_recipe = chefUser_data,rating = 5,desc = rating)



@then (u'I, the user "{user}", see my rating "{rating}" on the recipe "{recipe}" made by the other user "{chefUser}"')
def step_impl(context,user, rating, recipe,chefUser):
    assert context.browser.is_text_present('User Profile')
    assert context.browser.is_text_present(user)
    assert context.browser.is_text_present(rating)
    assert context.browser.is_text_present(recipe)
    assert context.browser.is_text_present(chefUser)


