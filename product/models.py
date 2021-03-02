from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django_countries.fields import CountryField



# Possui informações dos produtos


class Product(models.Model):

    condition_type = (
        ("New","Novo"),
        ("Semi_new","Semi-novo"),
        ("Used","Usado"),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Quando um usuário for deletado do banco, seus produtos também serão.
    now = datetime.now()
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=400)
    condition =  models.CharField(max_length=100,choices=condition_type)
    category =  models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    brand= models.ForeignKey('Brand',on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    created = models.DateTimeField(default=now)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/',blank=True,null=True)

    class Meta:
        verbose_name = 'Imagem do Produto'
        verbose_name_plural = 'Imagens do Produto'

    def __str__(self):
        return self.product.name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=60)
    brand_nationality = CountryField()

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.brand_name
