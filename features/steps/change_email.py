from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")

@given(u'I click on profile button')
def step_impl(context):
    toggle_down_navbar(context)
    profile_btn = context.browser.find_by_id('profile-btn')
    profile_btn.click()
    assert context.browser.is_text_present("User Profile")


@when(u'I click on change email button')
def step_impl(context):
    email_btn = context.browser.find_by_id('email-btn')
    email_btn.click()
    assert context.browser.is_text_present("Change Email")


@when(u'I fill the camps with my new email "{new_email}"')
def step_impl(context, new_email):
    form = context.browser.find_by_tag('form')
    context.browser.fill('new_email1', new_email)
    context.browser.fill('new_email2', new_email)
    form.find_by_css('button[type="submit"]').first.click()



@then(u'I click on change email button')
def step_impl(context):
    email_btn = context.browser.find_by_id('email-btn')
    email_btn.click()
    assert context.browser.is_text_present("Change Email")


@then(u'I fill the camps with my the same email "{same_email}"')
def step_impl(context, same_email):
    form = context.browser.find_by_tag('form')
    context.browser.fill('new_email1', same_email)
    context.browser.fill('new_email2', same_email)
    form.find_by_css('button[type="submit"]').first.click()


@then(u'It appears error message "{err_msg}"')
def step_impl(context, err_msg):
    assert context.browser.is_text_present(err_msg)