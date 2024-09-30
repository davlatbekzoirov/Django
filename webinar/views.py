from django.shortcuts import render, redirect
from .models import Meeting

def meeting_list(request):
    meetings = Meeting.objects.all() 
    return render(request, 'meetings/meeting_list.html', {'meetings': meetings})

def meeting_room(request, room_name):
    return render(request, 'meetings/meeting_room.html', {'room_name': room_name})

def create_meeting(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')

        meeting = Meeting.objects.create(room_name=room_name)

        return redirect('meeting_room', room_name=meeting.room_name)

    return render(request, 'meetings/create_meeting.html')
