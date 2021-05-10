from behave import *
from django.contrib.auth.models import User

use_step_matcher("parse")
#Test 1
@given(u'Exists a User "{user}" and I\'m logged with it in order to visit my profile')
def step_impl(context,user):
    createdUser = User.objects.create_user(username=user, email='testbehave@potatoe.com', password='Exemple123')
    context.browser.visit(context.get_url("/profile/"))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', user)
    context.browser.fill('password', 'Exemple123')
    form.find_by_id('Iniciar Sessió').first.click()
    
@when(u'I go to my profile and change my password "{password}"')
def step_impl(context,password):
    form.find_by_id('buttonChangePassword').first.click()
    


@then(u'I\'ll be able to log out')
def step_impl(context):
    form.find_by_id('logout').first.click()

@then(u'I\'ll be able to logging with the new password "{password}"')
def step_impl(context,user,password):
    context.browser.visit(context.get_url("/profile/"))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', user)
    context.browser.fill('password', password)
    form.find_by_id('Iniciar Sessió').first.click()
    assert context.browser.is_text_present('User Profile')


#Test 2 
#@given(u'')
#def step_impl(context,user):



#@when(u'')
#def step_impl(context):



#@then(u'')
#def step_impl(context):

#Test 23
#@given(u'')
#def step_impl(context,user):



#@when(u'')
#def step_impl(context):



#@then(u'')
#def step_impl(context):
