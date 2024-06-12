from django.contrib import admin
from .models import Add_jobs, Image, Image_job, AdminMessage
from .forms import AdminMessageForm


admin.site.register(Add_jobs)
admin.site.register(Image)
admin.site.register(Image_job)
class AdminMessageAdmin(admin.ModelAdmin):
    form = AdminMessageForm

admin.site.register(AdminMessage, AdminMessageAdmin)
