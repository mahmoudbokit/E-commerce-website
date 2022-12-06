from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now=True)

    class ByOrder:
        ordering = ['-date_added']

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.CharField(max_length=6000)
    date_added = models.DateTimeField(auto_now=True)

    class ByOrder:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


class Command(models.Model):
    items = models.CharField(max_length=350)
    totalQuantity = models.CharField(max_length=300)
    totalPrice = models.CharField(max_length=250)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    State = models.CharField(max_length=350)
    zipcode = models.CharField(max_length=350)
    date_command = models.DateTimeField(auto_now=True)

    class ByOrder:
        ordering = ['-date_command']


class Comment(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField()
    date_comment = models.DateTimeField(auto_now=True)

    class ByOrder:
        ordering = ['-date_command']
