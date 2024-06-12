# admin.py
from django.contrib import admin
from .models import Holiday, LabTemperature

class HolidayAdmin(admin.ModelAdmin):
    # Ro'yxatni ko'rish uchun kerakli qatorlar
    list_display = ('day_id', 'holiday', 'user_id')
    # Filtrlash uchun kerakli maydonlar
    list_filter = ('holiday',)
    # Qidiruv maydonlari
    search_fields = ('day_id', 'user_id')

class LabTemperatureAdmin(admin.ModelAdmin):
    # Ro'yxatni ko'rish uchun kerakli qatorlar
    list_display = ('lab_id', 'date', 'time', 'day', 'temp_inside', 'temp_outside', 'temp_dif')
    # Filtrlash uchun kerakli maydonlar
    list_filter = ('lab_id', 'date')
    # Qidiruv maydonlari
    search_fields = ('lab_id', 'date', 'time')

# Holiday modelini admin panelga qo'shish
admin.site.register(Holiday, HolidayAdmin)
# LabTemperature modelini admin panelga qo'shish
admin.site.register(LabTemperature, LabTemperatureAdmin)
