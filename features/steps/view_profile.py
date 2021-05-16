from behave import *
from django.contrib.auth.models import User
from DishDecoderApp.models import Ratings, Recipes

use_step_matcher("parse")
#Test 1    
@when(u'I\'ll try to see my profile through the url')
def step_impl(context):
    context.browser.visit(context.get_url("/profile/"))

@then(u'I\'ll be redirected to the login page')
def step_impl(context):
    assert context.browser.is_text_present('Log in')
    assert context.browser.is_text_present('Username')
    assert context.browser.is_text_present('Password')


#Test 2 
@then(u'I, as the user "{user}", will see my profile\'s information.')
def step_impl(context, user):
    assert context.browser.is_text_present('User Profile')
    foundh1 = context.browser.find_by_tag('h1')
    assert foundh1[1]
    assert foundh1[1].text == user

#Test3
@then (u'I will see in my profila that I made the recipe "{recipe}"')
def step_impl(context,recipe):
    assert context.browser.is_text_present('User Profile')
    assert context.browser.is_text_present(recipe)
    


#Test4
@given (u'I, the user "{user}", made a rating "{rating}" on the recipe "{recipe}"')
def step_impl(context,user, rating,recipe):
    user_data = User.objects.get(username=user)
    chefUser_data = Recipes.objects.get(name=recipe)
    Ratings.objects.create(id_autor = User.objects.get(id=user_data.id),id_recipe = chefUser_data,rating = 5,desc = rating)



@then (u'I, the user "{user}", will see my rating "{rating}" on the recipe "{recipe}" made by the other user "{chefUser}"')
def step_impl(context,user, rating, recipe,chefUser):
    assert context.browser.is_text_present('User Profile')
    assert context.browser.is_text_present(user)
    assert context.browser.is_text_present(rating)
    assert context.browser.is_text_present(recipe)
    assert context.browser.is_text_present(chefUser)


