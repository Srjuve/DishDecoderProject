from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")
@given(u'Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)

@given(u'I click on the login button')
def step_impl(context):
    context.browser.visit(context.get_url('/'))
    toggle_down_navbar(context)
    login_btn = context.browser.find_by_id('login-btn')
    login_btn.click()
    assert context.browser.is_text_present("Username")

@given(u'I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    form = context.browser.find_by_tag('form')
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_css('input[name="Log in"]').first.click()
    toggle_down_navbar(context)

@then(u'It appears my username "{username}"')
def step_impl(context, username):
    toggle_down_navbar(context)
    assert context.browser.is_text_present('Hello, ' + str(username))

@then(u'Login credentials invalid')
def step_impl(context):
    assert context.browser.is_text_present("Login credentials invalid")


@when(u'I click on logout button')
def step_impl(context):
    toggle_down_navbar(context)
    logout_btn = context.browser.find_by_id('logout-btn')
    logout_btn.click()
    toggle_down_navbar(context)
    assert context.browser.find_by_id('login-btn')


@then(u'I logout from the account')
def step_impl(context):
    assert not context.browser.find_by_id('logout-btn')


@when(u'I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    form = context.browser.find_by_tag('form')
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_css('input[name="Log in"]').first.click()
    


