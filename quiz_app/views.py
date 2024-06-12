from django.shortcuts import render
from django.views.generic import DeleteView
from .models import Add_jobs, Popular_course, Teacher


def main_page(request):
    try:
        logged_in = request.session["email"]
        all_jobs = Add_jobs.objects.all()
        add_course = Popular_course.objects.all()   
        teacher_info = Teacher.objects.all()
        return render(request, 'index.html', {'all_jobs': all_jobs, 'add_course': add_course, 'teacher_info': teacher_info, "ok": logged_in})
    except:
        return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def base(request):
    return render(request, 'base.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def course(request):
    return render(request, 'course.html')

def single(request):
    return render(request, 'single.html')

def teacher(request):
    return render(request, 'teacher.html')

