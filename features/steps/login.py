from behave import *

use_step_matcher("parse")
@given(u'Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)
    print("setup",username, password)

@given(u'I click on the login button')
def step_impl(context):
    context.browser.visit(context.get_url('/'))
    toggler_btn = context.browser.find_by_css('button[class="navbar-toggler"]')
    if toggler_btn:
        toggler_btn.click()
    login_btn = context.browser.find_by_id('login-btn')
    login_btn.click()
    assert context.browser.is_text_present("Username")

@given(u'I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    form = context.browser.find_by_tag('form')
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_css('input[name="Log in"]').first.click()
    toggler_btn = context.browser.find_by_css('button[class="navbar-toggler"]')
    if toggler_btn:
        toggler_btn.click()
    print(context.browser.html)
    print("out", username, password)
    print('Hello, ' + str(username))
    assert context.browser.is_text_present('Hello, ' + str(username))

@then(u'It appears my username "{username}"')
def step_impl(context, username):
    print(username)
    assert context.browser.is_text_present(str(username))


@given(u'I login as user "{foo}" with "{password}"')
def step_impl(context, foo, password):
    form = context.browser.find_by_tag('form')
    context.browser.fill('username', foo)
    context.browser.fill('password', password) 
    form.find_by_css('input[name="Log in"]').first.click()
    toggler_btn = context.browser.find_by_css('button[class="navbar-toggler"]')
    if toggler_btn:
        toggler_btn.click()
    assert not context.browser.is_text_present('Hello, ' + str(foo))



@then(u'Login credentials invalid')
def step_impl(context):
    assert context.browser.is_text_present("Login credentials invalid")