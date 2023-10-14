from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class Vacancy(models.Model):
    title = models.CharField(max_length=250)
    condition = models.TextField(max_length=1000)
    requirement = models.TextField(max_length=1000)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=100)
    img_url = models.ImageField()

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    size = models.CharField(max_length=100)
    painting = models.CharField(
        max_length=20,
        choices=(
            ('full', 'fully painted'),
            ('surface', 'surface painted'),
            ('other', 'other')
        ))
    number_pieces_in_sqr = models.CharField(max_length=100)
    weight_in_sqr = models.CharField(max_length=100)
    images = models.ManyToManyField(Image)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    images = models.ManyToManyField(Image)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.price