from django.db import models
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(verbose_name="Ism", max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    telegram_id = models.BigIntegerField(verbose_name='Telegram ID', unique=True, default=1)


    class Meta:
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.firstname + " " + self.lastname
