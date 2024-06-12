from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Product_mini(models.Model):
    USD = 'USD'
    UZS = 'UZS'
    CURRENCY_CHOICES = [
        (USD, 'DOLLARS'),
        (UZS, 'SO`M'),
    ]
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    product_name = models.CharField(max_length=350, null=True, verbose_name='Mahsulotning nomi')
    description = models.TextField(blank=True, verbose_name='Mahsulot haqida')
    olchov = models.CharField(max_length=350, blank=True, verbose_name='Olchovi')
    budget = models.IntegerField(default=0, verbose_name='Budget')
    price = models.CharField(max_length=10, verbose_name='KURS', choices=CURRENCY_CHOICES, default=USD)
    material = models.CharField(max_length=350, blank=True, verbose_name='Material')
    status = models.CharField(max_length=350, blank=True, verbose_name='Holati')
    kafolat = models.CharField(max_length=350, blank=True, verbose_name='Kafolat')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    category_code = models.CharField(max_length=20, verbose_name='Kategoriya kodi')
    category_name = models.CharField(max_length=30, verbose_name='Kategoriya nomi')
    subcategory_code = models.CharField(max_length=20, verbose_name='Ost-kategoriya kodi')
    subcategory_name = models.CharField(max_length=30, verbose_name='Ost-kategoriya nomi')
    class Meta:
        ordering = ['product_name']
        verbose_name = 'Product Mini'
        verbose_name_plural = 'Product Mini'
    
    def str(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('')
   
class Product_max(models.Model):
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    product_name = models.CharField(max_length=350, null=True, verbose_name='Mahsulotning nomi')
    description = models.TextField(blank=True, verbose_name='Mahsulot haqida')
    company = models.CharField(max_length=350 ,blank=True, verbose_name='Mahsulotning kompaniyasi')
    mahsulot = models.CharField(max_length=350, blank=True, verbose_name='Kompniyaning mahsuloti')
    olchov = models.CharField(max_length=350, blank=True, verbose_name='Olchovi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi')
    material = models.CharField(max_length=350, blank=True, verbose_name='Material')
    status = models.CharField(max_length=350, blank=True, verbose_name='Holati')
    kafolat = models.CharField(max_length=350, blank=True, verbose_name='Kafolat')

    class Meta:
        ordering = ['product_name']
        verbose_name = 'Product Max'
        verbose_name_plural = 'Product Max'
    
    def __str__(self):
        return self.product_name