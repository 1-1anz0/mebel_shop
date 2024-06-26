from django.db import models
from users.models import Users
from goods.models import Products
# Create your models here.


class CartsQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        else:
            return 0

class Carts(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Ulanyjy')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Onum')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Mukdary')
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Tazelenen wagty')

    class Meta:

        verbose_name = 'Sebet'
        verbose_name_plural = 'Sebet'
    
    objects = CartsQueryset().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f'Sebet {self.user.username} | Onumler {self.product} | Mukdary {self.quantity}'