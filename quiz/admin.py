from django.contrib import admin

from .models import Category,Task,Taskusers


@admin.register(Taskusers)
class TaskusersAdmin(admin.ModelAdmin):
    list_display = ("username", "category", "natija","checking")
    list_filter = ('checking',)
    list_editable = ('checking',) 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ( "title","category",)
    list_filter = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title","count_task")
    list_editable = ("count_task",)

