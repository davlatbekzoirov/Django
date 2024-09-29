# webinars/admin.py
from django.contrib import admin
from .models import Meeting, Participant

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'created_at', 'meeting_id')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['webinar', 'user', 'registered_at']
    search_fields = ['user__username', 'webinar__title']
