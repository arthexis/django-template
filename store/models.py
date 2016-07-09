from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )


class Product(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, 'products')
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)


class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, 'customers')


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, models.PROTECT)
    product = models.ForeignKey(Product, models.PROTECT)
    quantity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='in_progress')
    paid_on = models.DateTimeField(null=True)
    reference = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ('updated_on', )




