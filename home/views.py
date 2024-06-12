from django.shortcuts import render, redirect
from .models import Add_jobs, Image, Image_job, AdminMessage
from django.views.generic import DeleteView
from .forms import MyForm, AdminMessageForm

def homepage(request):
    try:
        logged_in = request.session["email"]
        all_jobs = Add_jobs.objects.all()
        imageall = Image.objects.all()    
        image_job = Image_job.objects.all()    
        return render(request, 'index.html', {'all_jobs': all_jobs, "ok": logged_in, "imageall": imageall, "image_job": image_job})
    except:
        return render(request, 'index.html')
    
def add_jobs(request):
    try:
        user = request.session["email"]
        formacha = MyForm(request.POST)
        if user:
            if request.method == "POST":
                form = MyForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect("/")
                else:
                    return redirect("add_jobs/")
            elif request.method == "GET":
                return render
            
            (request, 'add_jobs.html', {"form": formacha})
        else:
            return redirect("/not_access")
    except Exception as ex:
        print(ex)
        return redirect('/')
    
def not_access(request):
    return render(request, 'not_access.html')

class Job(DeleteView):
    model = Add_jobs
    template_name = 'message.html'
    context_object_name = "job"

def message_about(request):
    if request.method == 'POST':
        msg = AdminMessageForm(request.POST)
        if msg.is_valid():
            msg.save()
            return redirect('/') 
    else:
        msg = AdminMessageForm()

    return render(request, 'message.html', {'msg_message': msg})