from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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
    img_url = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
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
    # user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.SmallIntegerField(default=1)
    total = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(
        max_length=50,
        choices=(
            ('Order', 'Order accepted'),
            ('Produced', 'The product is produced'),
            ('Delivered', 'The order has been delivered')
        )
    )
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username


class Service(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    images = models.ManyToManyField(Image)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00)

    def __str__(self):
        return f"{self.product} | {self.color} | {self.price}"