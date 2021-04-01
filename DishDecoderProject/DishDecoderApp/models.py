from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
#from django.conf import settings
# Create your models here.
class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='recipeauthor')
    steps = models.CharField(max_length=2000)
    basic_products = models.ManyToManyField('BasicProducts',through='Recipe_Product')
    recipe_ratings = models.ManyToManyField(settings.AUTH_USER_MODEL,through='Ratings')

    def __str__(self):
        return self.name

class BasicProducts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    unit = models.CharField(max_length=12)
    nutrients = models.ManyToManyField('Nutrients',through='Product_Nutrients')

    def __str__(self):
        return self.name

class Nutrients(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Ratings(models.Model):
    id = models.AutoField(primary_key=True)
    id_autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    id_recipe = models.ForeignKey(Recipes,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0,validators=[MaxValueValidator(10),MinValueValidator(0)])
    desc = models.CharField(max_length=1000)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['id_autor','id_recipe'],name="unique_key_pairs_autor_recipe"),]

class Recipe_Product(models.Model):
    id = models.AutoField(primary_key=True)
    id_recipe = models.ForeignKey(Recipes,on_delete=models.CASCADE)
    id_product = models.ForeignKey(BasicProducts,on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6,decimal_places=3,default=0,validators=[MinValueValidator(0)])
    class Meta:
        constraints = [models.UniqueConstraint(fields=['id_recipe','id_product'],name="unique_key_pairs_recipe_product"),]


class Product_Nutrients(models.Model):
    id = models.AutoField(primary_key=True)
    id_product = models.ForeignKey(BasicProducts,on_delete=models.CASCADE)
    id_nutrient = models.ForeignKey(Nutrients,on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6,decimal_places=3,default=0,validators=[MinValueValidator(0)])
    class Meta:
        constraints = [models.UniqueConstraint(fields=['id_product','id_nutrient'],name="unique_key_pairs_product_nutrient"),]
    

