from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")

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


@then(u'I logout from the account')
def step_impl(context):
    assert not context.browser.find_by_id('logout-btn')


@when(u'I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    form = context.browser.find_by_tag('form')
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_css('input[name="Log in"]').first.click()
    


