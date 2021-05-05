from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import *
from django.contrib.auth.models import User
use_step_matcher("parse")
#test1

@when(u'I register as username "{username}" with mail "{mail}" and password "{pasw}"')
def step_impl(context,username,mail,pasw):
    toggle_down_navbar(context)
    context.browser.visit(context.get_url("/register/"))
    form = context.browser.find_by_tag('form')
    context.browser.fill('username', username)
    context.browser.fill('email',mail)
    context.browser.fill('password1',pasw)
    context.browser.fill('password2',pasw)
    form.find_by_css('input[name="Create User"]').first.click()

@then(u'I see the login page, i log in with my username "{username}" and password "{pasw}"')
def step_impl(context,username,pasw):
    form = context.browser.find_by_tag('form')
    context.browser.fill('username', username)
    context.browser.fill('password',pasw)
    form.find_by_css('input[name="Log in"]').first.click()
    toggle_down_navbar(context)

@then(u'It appears my username "{username}"')
def step_impl(context,username):
    toggle_down_navbar(context)
    assert context.browser.is_text_present('Hello, ' + str(username))

def toggle_down_navbar(context):
    toggler_btn = context.browser.find_by_css('button[class="navbar-toggler"]')
    if toggler_btn:
        toggler_btn.click()
