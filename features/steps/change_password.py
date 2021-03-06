from behave import *
from django.contrib.auth.models import User

use_step_matcher("parse")

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

@when(u'I introduce my old password as "{oldPassword}" and the password that I want as "{newPassword}"')
def step_impl(context, oldPassword, newPassword):
    context.browser.links.find_by_text('Change Password').first.click()
    context.browser.fill('old_password', oldPassword)
    context.browser.fill('new_password1', newPassword)
    context.browser.fill('new_password2', newPassword)
    context.browser.find_by_id('submit-password').first.click()
