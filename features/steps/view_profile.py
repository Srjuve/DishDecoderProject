from behave import *

use_step_matcher("parse")
#Test 1
@given(u'Exists a User "{id}" but it\'s not logged')   ##No ser si el camp es id, haig de mirar el model
def step_impl(context,id):
    

@when(u'I,"{id}", try to see my profile')
def step_impl(context,id):
    

@then(u'I\'ll receive an error')
def step_impl(context):
    

#Test 2
@given(u'Exists a User "{id}" and it\'s logged ')
def step_impl(context,id):
    

@when(u'I, "{id}", try to see my profile')
def step_impl(context,id):
    

@then(u'I\'ll bee seeing my profile\'s information')
def step_impl(context):


#Test 3
@given(u'Exists a User "{id}" and it\'s logged')
def step_impl(context,id):
    

@when(u'I, "{id}", try to see my profile')
def step_impl(context,id):
    

@then(u'I\'m expecting to receive an error')
def step_impl(context):