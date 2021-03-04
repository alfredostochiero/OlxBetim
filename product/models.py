from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# from django.db.models import signals
from django.utils.text import slugify


# Possui informações dos produtos


class Product(models.Model):

    condition_type = (
        ("Novo","Novo"),
        ("Semi-novo","Semi-novo"),
        ("Usado","Usado"),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Quando um usuário for deletado do banco, seus produtos também serão.
    now = datetime.now()
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=400)
    condition =  models.CharField(max_length=100,choices=condition_type)
    category =  models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    brand= models.ForeignKey('Brand',on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='main_product/', blank=True, null=True)
    created = models.DateTimeField(default=now)
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)




class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/',blank=True,null=True)

    class Meta:
        verbose_name = 'Imagem do Produto'
        verbose_name_plural = 'Imagens do Produto'

    def __str__(self):
        return self.product.name

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)


class Brand(models.Model):
    brand_name = models.CharField(max_length=60)
    brand_nationality = CountryField()

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.brand_name



