from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    username = models.CharField(verbose_name="Telegram username", max_length=100, null=True)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)
    email = models.CharField(verbose_name='Email', max_length=50, null=True)
    debt = models.DecimalField(verbose_name="Qarz", decimal_places=2, max_digits=8, null=True, default=0) 

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.full_name} - Qarz: {self.debt}"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    productname = models.CharField(verbose_name="Mahsulot nomi", max_length=50)
    photo = models.ImageField(verbose_name="Rasm file", upload_to='product_photos', null=True)
    price = models.DecimalField(verbose_name="Narx", decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name="Mahsulot haqida", max_length=3000, null=True)

    category_code = models.CharField(verbose_name="Kategoriya kodi", max_length=20)
    category_name = models.CharField(verbose_name="Kategoriya nomi", max_length=30)
    subcategory_code = models.CharField(verbose_name="Ost-kategoriya kodi", max_length=20)
    subcategory_name = models.CharField(verbose_name="Ost-kategoriya nomi", max_length=30)


    def __str__(self):
        return f"№{self.id} - {self.productname}"

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name="Ism", max_length=100)
    item_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, verbose_name="Telefon")
    shipping_address = models.CharField(max_length=100, verbose_name="Manzil")

    def __str__(self) -> str:
        return f"{self.id} - {self.item_id} - {self.phone_number} - {self.shipping_address}"
