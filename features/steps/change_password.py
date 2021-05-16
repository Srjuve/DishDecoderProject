from behave import *
from django.contrib.auth.models import User

use_step_matcher("parse")
#Test 1   
@when(u'I change my old password "{oldpassword}" to a new one "{newpassword}"')
def step_impl(context, oldpassword, newpassword):
    context.browser.links.find_by_text('Change Password').first.click()
    context.browser.fill('old_password', oldpassword)
    context.browser.fill('new_password1', newpassword)
    context.browser.fill('new_password2', newpassword)
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
@when(u'I\'ll try to enter to the site in which I should be able to change my password directly through the url')
def step_impl(context):
   context.browser.visit(context.get_url("/profile/change_password"))


@then(u'I\'ll be redirected since I\'m not logged in, requiring me to do it')
def step_impl(context):
    assert context.browser.is_text_present('Log in')
    assert context.browser.is_text_present('If you are not Registered go click')



#Test 3
@when(u'I change my password but I fail introducing the actual one')
def step_impl(context):
    context.browser.links.find_by_text('Change Password').first.click()
    context.browser.fill('old_password', 'contrasenyaEquivocada')
    context.browser.fill('new_password1', '123')
    context.browser.fill('new_password2', '123')
    context.browser.find_by_id('submit-password').first.click()


@then(u'The system will tell me that I entered invalid data')
def step_impl(context):
    assert context.browser.is_text_present('Invalid data entered')