from behave import *
from django.contrib.auth.models import User

use_step_matcher("parse")
#Test 1
@given(u'Exists a User "{user}" but it\'s not logged')
def step_impl(context,user):
    createdUser = User.objects.create_user(username=user, email='testbehave@potatoe.com', password='Exemple123')
    
@when(u'')
def step_impl(context):


@then(u'')
def step_impl(context):



#Test 2 
@given(u'')
def step_impl(context,user):



@when(u'')
def step_impl(context):



@then(u'')
def step_impl(context):

#Test 23
@given(u'')
def step_impl(context,user):



@when(u'')
def step_impl(context):



@then(u'')
def step_impl(context):
