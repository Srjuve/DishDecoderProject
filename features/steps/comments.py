from behave import *
from DishDecoderApp.models import *
from DishDecoderApp.views import *
from django.contrib.auth.models import User

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
        
    #assert "1"=="2" per a veure el html de la pagina per a la part dels comments dels users
