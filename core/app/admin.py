from django.contrib import admin
from .models import Product, Price, Color, Image, Service, Vacancy, Category

admin.site.register(Product)
admin.site.register(Price)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(Service)
admin.site.register(Vacancy)
admin.site.register(Category)