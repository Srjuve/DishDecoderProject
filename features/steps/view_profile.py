from behave import *
from django.contrib.auth.models import User
from DishDecoderApp.models import Ratings, Recipes

use_step_matcher("parse")
#Test 1    
@when(u'I\'ll try to see my profile through the url')
def step_impl(context):
    context.browser.visit(context.get_url("/profile/"))

@then(u'I\'ll receive an error')
def step_impl(context):
    assert context.browser.is_text_present('Log in')
    assert context.browser.is_text_present('Username')
    assert context.browser.is_text_present('Password')


#Test 2 
@then(u'I\'ll see the user\'s profile\'s information.')
def step_impl(context):
    assert context.browser.is_text_present('User Profile')
    foundh1 = context.browser.find_by_tag('h1')
    assert foundh1[1]


#Test3
@given (u'I made the recipe "{recipe}"')
def step_impl(context,user,recipe,password):
    createdUser = User.objects.create_user(username=user, email='testbehave@potatoe.com', password=password)
    Recipes.objects.create(name=recipe,author=createdUser,steps="Podria tenir tomata")
    context.browser.visit(context.get_url("/profile/"))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', user)
    context.browser.fill('password', password)
    form.find_by_id('submit-login').first.click()


@then (u'I, as user "UsuariTestBehave", will also see some details about his/her recipe "{recipe}"')
def step_impl(context,user,recipe):
    assert context.browser.is_text_present('User Profile')
    assert context.browser.is_text_present(recipe)
    


#Test4
@given (u'The user "{user}" with the password "{password}" is logged and he made a rating "{rating}" on the recipe "{recipe}" made by the other user "{chefUser}" with the password "{passwordChef}"')
def step_impl(context,user, password,rating,recipe,chefUser, passwordChef):
    createdChef = User.objects.create_user(username=chefUser, email='testchef@potatoe.com', password=passwordChef)
    createdRecipe = Recipes.objects.create(name=recipe,author=createdChef,steps="Podria tenir tomata")
    createdReviewer = User.objects.create_user(username=user, email='testReviewer@potatoe.com', password=password)
    Ratings.objects.create(id_autor = createdReviewer,id_recipe = createdRecipe,rating = 5,desc = rating)

    context.browser.visit(context.get_url("/profile/"))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', user)
    context.browser.fill('password', password)
    form.find_by_id('submit-login').first.click()

@then (u'The user "{user}" will also see some details about his/her rating "{rating}" on the recipe "{recipe}" made by the other user "{chefUser}"')
def step_impl(context,user, rating, recipe,chefUser):
    assert context.browser.is_text_present('User Profile')
    assert context.browser.is_text_present(user)
    assert context.browser.is_text_present(rating)
    assert context.browser.is_text_present(recipe)
    assert context.browser.is_text_present(chefUser)


