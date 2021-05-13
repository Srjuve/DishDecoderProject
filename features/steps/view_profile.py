from behave import *
from django.contrib.auth.models import User
from DishDecoderApp.models import Recipes

use_step_matcher("parse")
#Test 1
@given(u'Exists a User "{user}" but it\'s not logged')
def step_impl(context,user):
    createdUser = User.objects.create_user(username=user, email='testbehave@potatoe.com', password='Exemple123')
    
@when(u'I\'ll try to see my profile')
def step_impl(context):
    context.browser.visit(context.get_url("/profile/"))

@then(u'I\'ll receive an error')
def step_impl(context):
    assert context.browser.is_text_present('Log in')
    assert context.browser.is_text_present('Username')
    assert context.browser.is_text_present('Password')


#Test 2 
@given(u'I, as "{user}", am logged in the system')
def step_impl(context,user):
    createdUser = User.objects.create_user(username=user, email='testbehave@potatoe.com', password='Exemple123')
    #Em falta loggejar
    context.browser.visit(context.get_url("/profile/"))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', user)
    context.browser.fill('password', 'Exemple123')
    form.find_by_id('Iniciar Sessió').first.click()


@when(u'I\'m going to my profile')
def step_impl(context):
    context.browser.visit(context.get_url("/profile/"))


@then(u'I\'ll bee seeing my profile\'s information')
def step_impl(context):
    assert context.browser.is_text_present('User Profile')
    assert context.browser.is_text_present('Change password')
    assert context.browser.is_text_present('Change email')