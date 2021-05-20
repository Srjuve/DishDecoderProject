from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import *
from django.contrib.auth.models import User
from utils import toggle_down_navbar
use_step_matcher("parse")

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

@given(u'An account')
def step_impl(context):
    User.objects.create_user(username="patata",email="patata@patata.com",password="Exemple123")