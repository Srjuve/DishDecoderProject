from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import *
from django.contrib.auth.models import User

use_step_matcher("parse")
#test1
@given(u'Exist an username "{username}",and a mail "{mail}", and a password "{pasw}"')
def step_impl(context,username,mail,pasw):
    User.objects.create_user(username=username,email=mail,password=pasw)

@when(u'I register with username "{username}", mail "{mail}", password "{pasw}"')
def step_impl(context,username,mail,pasw):
    context.browser.visit(context.get_url("/register/"))
    toggler_btn = context.browser.find_by_css('button[class=navbar-toggler]')