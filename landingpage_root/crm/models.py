from django.db import models

# Create your models here.
class Order(models.Model):
    oder_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='имя заказчика')
    order_phone = models.CharField(max_length=200, verbose_name='номер телефона')
    
    def __str__(self):
        return self.order_name
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'