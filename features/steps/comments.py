from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import *
from django.contrib.auth.models import User


#test 1
use_step_matcher("parse")
@when(u'I fill the comment with "{desc}" with rate "{rating}"')
def step_impl(context, desc, rating):
    form = context.browser.find_by_tag('form')
    context.browser.fill('desc', desc)
    context.browser.fill('rating',rating)


@when(u'I click on summit comment button')
def step_impl(context):
    create_btn = context.browser.find_by_id('id_comment')
    create_btn.click()

@then(u'I view the comment in the recipe with name "{rename}" by "{user}"')
def step_impl(context,rename, user):
    reciperating = context.browser.find_by_id('recipe_rating').text
    user_data = User.objects.get(username=user)
    recipe_data = Recipes.objects.get(name=rename)
    rating_data = Ratings.objects.get(id_autor=user_data,id_recipe=recipe_data)
    assert reciperating == "Rating: 8.00"
    review_container = context.browser.find_by_id('review-container').find_by_id('review')[-1]
    assert review_container.find_by_tag("h5").text == user
    assert review_container.find_by_tag("p").text == rating_data.desc
    assert review_container.find_by_tag("button").text == str(rating_data.rating)+" out of 10"
        
#test3
@then(u'I see an error saying i can not leave two reviews')
def step_impl(context):
    error = context.browser.find_by_id('Comment_error')
    assert error.text == "Only one review per user and recipe"
#"Comment_error"
@then(u'I fill the comment with "{desc}" with rate "{rating}"')
def step_impl(context, desc, rating):
    form = context.browser.find_by_tag('form')
    context.browser.fill('desc', desc)
    context.browser.fill('rating',rating)


@then(u'I click on summit comment button')
def step_impl(context):
    create_btn = context.browser.find_by_id('id_comment')
    create_btn.click()


