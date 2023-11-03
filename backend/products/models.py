from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)

    @property
    def sales_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    @staticmethod
    def get_discount():
        return "122"
