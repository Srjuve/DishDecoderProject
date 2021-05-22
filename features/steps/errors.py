from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")


@then(u'It appears error message "{err_msg}"')
def step_impl(context, err_msg):
    assert context.browser.is_text_present(err_msg)


@then(u'I\'m expecting to recive error "{err_code}" with message "{err_msg}"')
def step_impl(context, err_code, err_msg):
    assert context.browser.is_text_present(err_code)
    assert context.browser.is_text_present(err_msg)

@then(u'I\'m viewing the 404 error page')
def step_impl(context):
    title = context.browser.find_by_tag('h1')
    assert title.text == "Error 404"

@then(u'I receive the error 404')
def step_impl(context):   
    assert context.browser.is_text_present('Error 404')
    assert context.browser.is_text_present('The page you are trying to reach does not exist')

@then(u'I can see that there\'s no description')
def step_impl(context):
    assert context.browser.is_text_present('No Data Found')

@then(u'I see the incorrect number of Ingredients exceptions')
def step_impl(context):
    error_message = context.browser.find_by_id('error_messages').find_by_tag('li')
    assert error_message.text == "Incorrect number of ingredients"

@then(u'I see the quantity value too big error')
def step_impl(context):
    error_message = context.browser.find_by_id('error_messages').find_by_tag('li')
    assert error_message.text == "Ingredient quantity too big(0-999)"

@then(u'I see the invalid ingredient format error')
def step_impl(context):
    error_message = context.browser.find_by_id('error_messages').find_by_tag('li')
    assert error_message.text == "Incorrect Ingredient format"

@then(u'I see the repeated ingredient error')
def step_impl(context):
    error_message = context.browser.find_by_id('error_messages').find_by_tag('li')
    assert error_message.text == "Ingredient already set"

@then(u'I see an error saying i can not leave two reviews')
def step_impl(context):
    error = context.browser.find_by_id('Comment_error')
    assert error.text == "Only one review per user and recipe"

@then(u'The system tells me that I entered invalid data')
def step_impl(context):
    assert context.browser.is_text_present('Invalid data entered')

@then(u'Login credentials invalid')
def step_impl(context):
    assert context.browser.is_text_present("Login credentials invalid")

@then(u'This basic product details page shows no recipe')
def step_impl(context):
    assert context.browser.is_text_present('No Data Found')
