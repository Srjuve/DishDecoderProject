# Generated by Django 3.1.6 on 2021-04-08 16:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('unit', models.CharField(choices=[('g', 'Gram'), ('L', 'Litre')], default='g', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Nutrients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('desc', models.CharField(max_length=1000)),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=3, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DishDecoderApp.basicproducts')),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('steps', models.CharField(max_length=2000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipeauthor', to=settings.AUTH_USER_MODEL)),
                ('basic_products', models.ManyToManyField(through='DishDecoderApp.Recipe_Product', to='DishDecoderApp.BasicProducts')),
                ('recipe_ratings', models.ManyToManyField(through='DishDecoderApp.Ratings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='recipe_product',
            name='id_recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DishDecoderApp.recipes'),
        ),
        migrations.AddField(
            model_name='ratings',
            name='id_recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DishDecoderApp.recipes'),
        ),
        migrations.CreateModel(
            name='Product_Nutrients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=3, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ('id_nutrient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DishDecoderApp.nutrients')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DishDecoderApp.basicproducts')),
            ],
        ),
        migrations.AddField(
            model_name='basicproducts',
            name='nutrients',
            field=models.ManyToManyField(through='DishDecoderApp.Product_Nutrients', to='DishDecoderApp.Nutrients'),
        ),
        migrations.AddConstraint(
            model_name='recipe_product',
            constraint=models.UniqueConstraint(fields=('id_recipe', 'id_product'), name='unique_key_pairs_recipe_product'),
        ),
        migrations.AddConstraint(
            model_name='ratings',
            constraint=models.UniqueConstraint(fields=('id_autor', 'id_recipe'), name='unique_key_pairs_autor_recipe'),
        ),
        migrations.AddConstraint(
            model_name='product_nutrients',
            constraint=models.UniqueConstraint(fields=('id_product', 'id_nutrient'), name='unique_key_pairs_product_nutrient'),
        ),
    ]
