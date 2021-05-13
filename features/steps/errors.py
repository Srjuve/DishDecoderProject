from behave import *

from utils import toggle_down_navbar

use_step_matcher("parse")


@then(u'It appears error message "{err_msg}"')
def step_impl(context, err_msg):
    assert context.browser.is_text_present(err_msg)