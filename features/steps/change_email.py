from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")



@then(u'It appears my new email "{email}"')
def step_impl(context, email):
    assert context.browser.is_text_present(email)


@when(u'I fill the camps with my new email "{new_email}"')
def step_impl(context, new_email):
    form = context.browser.find_by_tag('form')
    context.browser.fill('new_email1', new_email)
    context.browser.fill('new_email2', new_email)
    form.find_by_css('button[type="submit"]').first.click()


@when(u'I fill first field with my new email "{new_email}"')
def step_impl(context, new_email):
    form = context.browser.find_by_tag('form')
    context.browser.fill('new_email1', new_email)



@when(u'I fill second field with my new email "{new_email}"')
def step_impl(context, new_email):
    form = context.browser.find_by_tag('form')
    context.browser.fill('new_email2', new_email)


@when(u'I submit the form')
def step_impl(context):
    form = context.browser.find_by_tag('form')
    form.find_by_css('button[type="submit"]').first.click()
