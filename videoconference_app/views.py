from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Meeting, Participant
import uuid

def create_meeting(request):
    if request.method == "POST":
        title = request.POST.get('title')
        meeting_id = str(uuid.uuid4())  # Generate a unique meeting ID
        meeting = Meeting.objects.create(title=title, host=request.user, meeting_id=meeting_id)
        return redirect('meeting_detail', meeting_id=meeting.meeting_id)
    return render(request, 'create_meeting.html')

def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, meeting_id=meeting_id)
    return render(request, 'meeting_detail.html', {'meeting': meeting})

def webinar_list(request):
    webinars = Meeting.objects.all().order_by('created_at')
    return render(request, 'webinars/webinar_list.html', {'webinars': webinars})

@login_required
def register_for_webinar(request, pk):
    webinar = get_object_or_404(Meeting, pk=pk)
    Participant.objects.get_or_create(webinar=webinar, user=request.user)
    return redirect('meeting_detail', meeting_id=webinar.meeting_id)
