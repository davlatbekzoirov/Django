# models.py
from django.db import models

class Holiday(models.Model):
    day_id = models.IntegerField()  #  Haftaning kuni uchun ma'lumotlar jadvali mavjud bo'lsa
    holiday = models.BooleanField(default=False) # Ta'til kuni uchun belgi
    user_id = models.IntegerField() # Foydalanuvchi ID si

    def __str__(self):
        return f"Holiday {self.day_id} - {self.holiday}"
    
class LabTemperature(models.Model):
    lab_id = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    day = models.IntegerField()
    temp_inside = models.FloatField()
    temp_outside = models.FloatField()
    temp_dif = models.FloatField(editable=False)
    
    def save(self, *args, **kwargs):
        self.temp_dif = self.temp_outside - self.temp_inside
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Lab {self.lab_id} - {self.date} {self.time}"
