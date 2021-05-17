from behave import *
from django.contrib.auth.models import User

use_step_matcher("parse")
#Test 1
@given(u'Exists a User "{user}" and I\'m logged with it')
def step_impl(context,user):
    createdUser = User.objects.create_user(username=user, email='testbehave@potatoe.com', password='Exemple123')
    context.browser.visit(context.get_url("/profile/"))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', user)
    context.browser.fill('password', 'Exemple123')
    #Podria buscar el nom enlloc d'afegir una id
    form.find_by_id('submit-login').first.click()
    
@when(u'I go to my profile and change my password "{password}"')
def step_impl(context,password):
    
    context.browser.visit(context.get_url("/profile/"))
    context.browser.links.find_by_text('Change Password').first.click()
    
    context.browser.fill('old_password', 'Exemple123')
    context.browser.fill('new_password1', password)
    context.browser.fill('new_password2', password)
    context.browser.find_by_id('submit-password').first.click()




@then(u'I\'ll be able to logging with the username "{user}" and the new password "{password}"')
def step_impl(context,user,password):
    context.browser.visit(context.get_url("/profile/"))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', user)
    context.browser.fill('password', password)
    form.find_by_id('submit-login').first.click()
    context.browser.visit(context.get_url("/profile/"))
    assert context.browser.is_text_present('User Profile')


#Test 2 
@given(u'Exists a User "{user}" but I\'m not logged') #Pot ser borrar?
def step_impl(context,user):
    createdUser = User.objects.create_user(username=user, email='testbehave@potatoe.com', password='Exemple123')

@when(u'I\'ll try to enter to the site in which I should be able to change my password')
def step_impl(context):
   context.browser.visit(context.get_url("/profile/change_password"))


@then(u'I\'ll be redirected, requiring me to log in')
def step_impl(context):
    assert context.browser.is_text_present('Log in')
    assert context.browser.is_text_present('If you are not Registered go click')



#Test 3
@given(u'Exists a User "{user}" with which I\'m logged in')
def step_impl(context,user):
    createdUser = User.objects.create_user(username=user, email='testbehave@potatoe.com', password='Exemple123')
    context.browser.visit(context.get_url("/profile/"))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', user)
    context.browser.fill('password', 'Exemple123')
    form.find_by_id('submit-login').first.click()


@when(u'I\'m going to change my password and fail')
def step_impl(context):
    context.browser.visit(context.get_url("/profile/"))
    context.browser.links.find_by_text('Change Password').first.click()
    
    context.browser.fill('old_password', 'contrasenyaEquivocada')
    context.browser.fill('new_password1', '123')
    context.browser.fill('new_password2', '123')
    context.browser.find_by_id('submit-password').first.click()


@then(u'The system will tell me that I entered invalid data')
def step_impl(context):
    assert context.browser.is_text_present('Invalid data entered')