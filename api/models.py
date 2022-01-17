from django.db import models
from django.db.models.base import ModelState

class Product(models.Model):
    EAN_13 = models.TextField(primary_key=True) 
    name = models.CharField(max_length=13)
    vat_rate = models.FloatField()
    price_in_cents = models.IntegerField()
    amount = models.IntegerField(default=100)
    threshold = models.IntegerField(default=10)

    def __str__(self):
        return self.name
    
# class Stocks(models.Model):
#     stock_id = models.AutoField(primary_key=True)
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     amount = models.IntegerField()
#     threshold = models.IntegerField()

#     def __str__(self):
#         return self.product_id

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    price = models.IntegerField()

    def __str__(self):
        return self.id

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.order_id