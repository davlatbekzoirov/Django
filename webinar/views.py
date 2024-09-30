from django.shortcuts import render, redirect

def meeting_room(request, room_name):
    return render(request, 'meetings/meeting_room.html', {'room_name': room_name})

def create_meeting(request):
    room_name = 'meeting-room-123'  # yoki o'zgaruvchini yarating
    return render(request, 'meetings/create_meeting.html', {'room_name': room_name})
