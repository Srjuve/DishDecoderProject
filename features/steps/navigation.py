from behave import *

from utils import toggle_down_navbar
from DishDecoderApp.models import *


use_step_matcher("parse")

@when(u'I click at submit autocomplete button')
def step_impl(context):
    ac_div = context.browser.find_by_id('autocomplete-div')
    ac_div.find_by_tag('input')[-1].click()

@when(u'Select first autocomplete options')
def step_impl(context):
    item_list = context.browser.find_by_id('ui-id-1')
    first_item = item_list.find_by_tag('li')[0]
    first_item.click()

@given(u'I click on the login button')
def step_impl(context):
    context.browser.visit(context.get_url('/'))
    toggle_down_navbar(context)
    login_btn = context.browser.find_by_id('login-btn')
    login_btn.click()
    assert context.browser.is_text_present("Username")

@when(u'I click on logout button')
def step_impl(context):
    toggle_down_navbar(context)
    logout_btn = context.browser.find_by_id('logout-btn')
    logout_btn.click()
    toggle_down_navbar(context)
    assert context.browser.find_by_id('login-btn')

@given(u'I click on profile button')
@when(u'I click on profile button')
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

@then(u'I click on change email button')
def step_impl(context):
    email_btn = context.browser.find_by_id('email-btn')
    email_btn.click()
    assert context.browser.is_text_present("Change Email")

@when(u'I click on create recipe button')
def step_impl(context):
    create_btn = context.browser.find_by_id('create-btn')
    create_btn.click()

@when(u'I click on erase recipe button')
def step_impl(context):
    erase_btn = context.browser.find_by_id('erase-btn')
    erase_btn.click()

@when(u'I click the edit recipe button')
def step_impl(context):
    context.browser.visit(context.get_url('/'))
    edit_btn = context.browser.find_by_id('edit-btn')
    edit_btn.click()

@given(u'I am on main page')
def step_impl(context):
    context.browser.visit(context.get_url('/'))


@when(u'I search the nutrient id "{id}"')
def step_impl(context,id):
    context.browser.visit(context.get_url("/nutrient/"+id))

@when(u'I search the nutrient "{name}"')
def step_impl(context,name):
    from DishDecoderApp.models import Nutrients
    nutrientSearched = Nutrients.objects.get(name = name)
    context.browser.visit(context.get_url("/nutrient/"+str(nutrientSearched.id)))


@when(u'I search the basic product with name "{bpname}"')
def step_impl(context,bpname):
    from DishDecoderApp.models import BasicProducts
    context.browser.visit(context.get_url("/basicproduct/"+str(BasicProducts.objects.filter(name=bpname).first().id)))

@when(u'I search the basic product with id "{bpid}"')
def step_impl(context,bpid):
    context.browser.visit(context.get_url("/basicproduct/"+bpid))

@when(u'I search the recipe with name "{rename}"')
def step_impl(context,rename):
    from DishDecoderApp.models import Recipes
    context.browser.visit(context.get_url("/recipe/"+str(Recipes.objects.filter(name=rename).first().id)))

@when(u'I search the recipe with id "{rid}"')
def step_impl(context, rid):
    from DishDecoderApp.models import Recipes
    context.browser.visit(context.get_url("/recipe/{rid}"))

@then(u'I get redirected to the login page')
def step_impl(context):
    assert context.browser.is_text_present('Log in')
    assert context.browser.is_text_present('Username')
    assert context.browser.is_text_present('Password')

@when(u'I enter the site in which I should be able to change my password directly through the url "{url}"')
def step_impl(context,url):
   context.browser.visit(context.get_url(url))

@when(u'I check my profile through the url')
def step_impl(context):
    context.browser.visit(context.get_url("/profile/"))

@then(u'I stay at "{current_url}"')
def step_impl(context, current_url):
    assert context.browser.url.replace(context.get_url('/'), '/') == current_url