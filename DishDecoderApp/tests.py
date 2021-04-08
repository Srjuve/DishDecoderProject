from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from DishDecoderApp.models import Recipes
from DishDecoderApp.views import *
from .forms import Main_page_form
from django.contrib import auth
# Create your tests here.

class ListRecipesViewTestCase(TestCase):
    
    def setUp(self):
        user = User.objects.create_user(username="example",password="Potatoe123")
        Recipes.objects.create(id=1,name="Recepta1",author=user,steps="123")
        Recipes.objects.create(id=2,name="Potatoe1",author=user,steps="123")
        Recipes.objects.create(id=3,name="Potatoe2",author=user,steps="123")
        self.factory=RequestFactory()
        self.c = Client()

    def test_non_existing_recipe(self):
        simple_response = self.c.get('/recipes/',{'search':'Exemple'})
        request = self.factory.get('/recipes/',{'search':'Exemple'})
        self.assertEqual(simple_response.status_code, 200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/recipes.html")
        self.assertEqual(list(simple_response.context['listedtuples']),[])

    def test_unique_recipe(self):
        response = self.c.get('/recipes/',{'search':'Recep'}, follow=True)
        self.assertRedirects(response,'/recipe/1',status_code=302)
    
    def test_multiple_recipes(self):
        simple_response = self.c.get('/recipes/',{'search':'Pota'})
        request = self.factory.get('/recipes/',{'search':'Pota'})
        self.assertEqual(simple_response.status_code, 200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/recipes.html")
        self.assertEqual(list(simple_response.context['listedtuples']),list(Recipes.objects.filter(name__contains='Pota')))

    def test_incorrect_request(self):
        simple_response = self.c.get('/recipes/')
        self.assertEqual(simple_response.status_code, 400)

class ListBasicProductsViewTestCase(TestCase):

    def setUp(self):
        BasicProducts.objects.create(id=1,name="Producte1",desc="desc",unit="g")
        BasicProducts.objects.create(id=2,name="Potatoe1",desc="desc",unit="g")
        BasicProducts.objects.create(id=3,name="Potatoe2",desc="desc",unit="g")
        self.c = Client()

    def test_non_existing_recipe(self):
        simple_response = self.c.get('/basicproducts/',{'search':'Exemple'})
        self.assertEqual(simple_response.status_code, 200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/basicproducts.html")
        self.assertEqual(list(simple_response.context['listedtuples']),[])

    def test_unique_recipe(self):
        response = self.c.get('/basicproducts/',{'search':'Prod'}, follow=True)
        self.assertRedirects(response,'/basicproduct/1',status_code=302)
    
    def test_multiple_recipes(self):
        simple_response = self.c.get('/basicproducts/',{'search':'Pota'})
        self.assertEqual(simple_response.status_code, 200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/basicproducts.html")
        self.assertEqual(list(simple_response.context['listedtuples']),list(BasicProducts.objects.filter(name__contains='Pota')))


class ListNutrientsViewTestCase(TestCase):

    def setUp(self):
        Nutrients.objects.create(id=1,name="Nutrient1",desc="desc")
        Nutrients.objects.create(id=2,name="Potatoe1",desc="desc")
        Nutrients.objects.create(id=3,name="Potatoe2",desc="desc")
        self.c = Client()

    def test_non_existing_recipe(self):
        simple_response = self.c.get('/nutrients/',{'search':'Exemple'})
        self.assertEqual(simple_response.status_code, 200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/nutrients.html")
        self.assertEqual(list(simple_response.context['listedtuples']),[])

    def test_unique_recipe(self):
        response = self.c.get('/nutrients/',{'search':'Nutr'}, follow=True)
        self.assertRedirects(response,'/nutrient/1',status_code=302)
    
    def test_multiple_recipes(self):
        simple_response = self.c.get('/nutrients/',{'search':'Pota'})
        self.assertEqual(simple_response.status_code, 200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/nutrients.html")
        self.assertEqual(list(simple_response.context['listedtuples']),list(Nutrients.objects.filter(name__contains='Pota')))

class MainPageViewTestCase(TestCase):
    
    def setUp(self):
        self.c = Client()

    def test_get_main_page(self):
        simple_response = self.c.get('/')
        self.assertEqual(simple_response.status_code,200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/main.html")
        self.assertTrue(isinstance(simple_response.context['form'],Main_page_form))

    def test_post_data_redirect_recipes_main_page(self):
        simple_response = self.c.post('/',{'request_objective':1,'item_name':'Example'},follow=True)
        self.assertEqual(simple_response.redirect_chain,[('/recipes/?search=Example',302)])

    def test_post_data_redirect_basicproducts_main_page(self):
        simple_response = self.c.post('/',{'request_objective':2,'item_name':'Example'},follow=True)
        self.assertEqual(simple_response.redirect_chain,[('/basicproducts/?search=Example',302)])

    def test_post_data_redirect_nutrients_main_page(self):
        simple_response = self.c.post('/',{'request_objective':3,'item_name':'Example'},follow=True)
        self.assertEqual(simple_response.redirect_chain,[('/nutrients/?search=Example',302)])


class RecipeProfileTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        user = User.objects.create_user(username="example",password="Potatoe123")
        self.recipe=Recipes.objects.create(id=1,name="Recepta1",author=user,steps="#First Step.#Second Step.")
        self.product=BasicProducts.objects.create(id=1,name="Producte1",desc="desc",unit="g")
        self.nutrient=Nutrients.objects.create(id=1,name="Nutrient1",desc="desc")
        Ratings.objects.create(id=1,desc="Test",id_autor=user,id_recipe=self.recipe,rating=8)
        self.prod_nutrients=Product_Nutrients.objects.create(id=1,id_product=self.product,id_nutrient=self.nutrient,quantity=0.500)
        self.recipe_product=Recipe_Product.objects.create(id=1,id_recipe=self.recipe,id_product=self.product,quantity=100)

    def test_get_existing_profile(self):
        simple_response = self.c.get('/recipe/1')
        self.assertEqual(simple_response.status_code,200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/recipe.html")
        self.assertEqual(simple_response.context['steps'],['First Step.','Second Step.'])
        self.assertEqual(simple_response.context['recipe'],self.recipe)
        self.assertEqual(list(simple_response.context['rec_prod']),list(Recipe_Product.objects.filter(id_recipe=1)))
        self.assertEqual(simple_response.context['nut_value'],[[0.5, self.nutrient]])
        self.assertEqual(list(simple_response.context['rating_data']),list(Ratings.objects.filter(id_recipe=1).all()))
        self.assertEqual(simple_response.context['average_score'],8.0)

    def test_get_non_existing_profile(self):
        simple_response = self.c.get('/recipe/2')
        self.assertEqual(simple_response.status_code,404)



class BasicProductsProfileTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        user = User.objects.create_user(username="example",password="Potatoe123")
        self.recipe = Recipes.objects.create(id=1,name="Recepta1",author=user,steps="#First Step.#Second Step.")
        self.product = BasicProducts.objects.create(id=1,name="Producte1",desc="desc",unit="g")
        self.recipe_product = Recipe_Product.objects.create(id=1,id_recipe=self.recipe,id_product=self.product,quantity=100)

    def test_get_existing_profile(self):
        simple_response = self.c.get('/basicproduct/1')
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/basic_product.html")
        self.assertEqual(simple_response.status_code,200)
        self.assertEqual(list(simple_response.context['recipes_products']),list(Recipe_Product.objects.filter(id_product=1).all()))
        self.assertEqual(simple_response.context['basic_product'],BasicProducts.objects.get(id=1))

    def test_get_non_existing_profile(self):
        simple_response = self.c.get('/basicproduct/666')
        self.assertEqual(simple_response.status_code,404)


class NutrientsProfileTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        self.nutrient = Nutrients.objects.create(id=1,name="Nutrient1",desc="desc")
        
    def test_get_existing_nutrient(self):
        simple_response = self.c.get('/nutrient/1')
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/nutrient.html")
        self.assertEqual(simple_response.context['nutrient'],self.nutrient)

    def test_get_non_existing_profile(self):
        simple_response = self.c.get('/nurient/2')
        self.assertEqual(simple_response.status_code,404)


class authComponentsTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username="example",password="Potatoe123")
        self.factory = RequestFactory()

    def test_logout_not_authenticated(self):
        simple_response = self.c.get('/logout/',follow=True)
        user = auth.get_user(self.c)
        self.assertTrue( not user.is_authenticated)
        self.assertRedirects(simple_response,'/',status_code=302)


    def test_logout_authenticated(self):
        self.c.login(username="example",password="Potatoe123")
        simple_response = self.c.get('/logout/',follow=True)
        user = auth.get_user(self.c)
        self.assertTrue(not user.is_authenticated)
        self.assertRedirects(simple_response,'/',status_code=302)


    def test_get_login_authenticated(self):
        self.c.login(username="example",password="Potatoe123")
        simple_response = self.c.get('/login/',follow=True)
        user = auth.get_user(self.c)
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(simple_response,'/',status_code=302)

    def test_get_login_not_authenticated(self):
        simple_response = self.c.get('/login/')
        self.assertTemplateUsed(simple_response,template_name='DishDecoderApp/login.html')
        self.assertEqual(simple_response.status_code,200)

    def test_post_login_not_authenticated(self):
        simple_response = self.c.post('/login/',{'username':"example",'password':"Potatoe123"},follow=True)
        user = auth.get_user(self.c)
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(simple_response,'/',status_code=302)

    def test_post_login_authenticated(self):
        self.c.login(username="example",password="Potatoe123")
        simple_response = self.c.post('/login/',{'username':"example",'password':"Potatoe123"},follow=True)
        user = auth.get_user(self.c)
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(simple_response,'/',status_code=302)

    def test_get_register_authenticated(self):
        self.c.login(username="example",password="Potatoe123")
        simple_response = self.c.get('/register/',follow=True)
        user = auth.get_user(self.c)
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(simple_response,'/',status_code=302)

    def test_get_register_not_authenticated(self):
        simple_response = self.c.get('/register/')
        self.assertTemplateUsed(simple_response,template_name='DishDecoderApp/register.html')
        self.assertEqual(simple_response.status_code,200)

    def test_post_register_not_authenticated(self):
        self.assertTrue(not User.objects.filter(username="example2").exists())
        simple_response = self.c.post('/register/',{'username':"example2",'email':"example2@example.com",'password1':"NewPassword123",'password2':"NewPassword123"},follow=True)
        self.assertTrue(User.objects.filter(username="example2").exists())
        self.assertRedirects(simple_response,'/login/',status_code=302)

    def test_post_register_authenticated(self):
        self.c.login(username="example",password="Potatoe123")
        simple_response = self.c.post('/register/',{'username':"example2",'email':"example2@example.com",'password1':"NewPassword123",'password2':"NewPassword123"},follow=True)
        self.assertRedirects(simple_response,'/',status_code=302)

    def test_get_profile_not_authenticated(self):
        simple_response = self.c.get('/profile/',follow=True)
        self.assertRedirects(simple_response,'/login/?next=/profile/',status_code=302)

    def test_get_profile_authenticated(self):
        self.c.login(username="example",password="Potatoe123")
        simple_response = self.c.get('/profile/')
        self.assertEqual(simple_response.status_code,200)
        self.assertTemplateUsed(simple_response,"DishDecoderApp/user_profile.html")

    
class UserProfileTestCase(TestCase):
    
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username="example",password="Potatoe123")
    
    def test_get_profile_without_ratings(self):
        self.c.login(username="example",password="Potatoe123")
        simple_response = self.c.get('/profile/')
        self.assertEqual(simple_response.status_code,200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/user_profile.html")
        self.assertRaises(KeyError,lambda:simple_response.context['scored_recipes'])

    def test_get_profile_with_ratings(self):
        self.c.login(username="example",password="Potatoe123")
        recipe = Recipes.objects.create(id=1,name="Recepta1",author=self.user,steps="123")
        Ratings.objects.create(id=1,desc="Test",id_autor=self.user,id_recipe=recipe,rating=8)
        simple_response = self.c.get('/profile/')
        self.assertEqual(simple_response.status_code,200)
        self.assertTemplateUsed(simple_response,template_name="DishDecoderApp/user_profile.html")
        self.assertEqual(list(simple_response.context['scored_recipes']),list(Ratings.objects.filter(id_autor=self.user.id).all()))