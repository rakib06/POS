from django.db import models


# Create your models here.


class Product(models.Model):
    type = models.CharField(max_length=200, blank=False)  # name of the column
    price = models.FloatField(blank=False, default=0.00) #
    choices = (
        ('Available', 'Item ready to be purchased'), ('Sold', 'Item is Sold'),
        ('Restocking', 'Item restocking in few days')
    )
    status = models.CharField(max_length=50,choices=choices, default='Available')  # available, Sold, Restocking
    issues = models.CharField(max_length=200, default='NA')

    class Meta:
        abstract = True

    def __str__(self):
        return "Type : {0} Price: {1} ".format(self.type, self.price)


class Chair(Product):
    pass


class Bed(Product):
    pass


class Sofa(Product):
    pass


class Delivery(models.Model):
    pass


class Service(models.Model):
    pass


class Design(models.Model):
    pass
