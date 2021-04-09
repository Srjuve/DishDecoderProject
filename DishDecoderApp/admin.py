from django.contrib import admin
from .models import Recipes,BasicProducts,Nutrients,Ratings,Recipe_Product,Product_Nutrients
 #Register your models here.
admin.site.register(Recipes)
admin.site.register(BasicProducts)
admin.site.register(Nutrients)
admin.site.register(Ratings)
admin.site.register(Recipe_Product)
admin.site.register(Product_Nutrients)
