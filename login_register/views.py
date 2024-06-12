from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Users
# from django.contrib.sessions import 
import smtplib

def notFound(request):
    return HttpResponseNotFound("<h1>Page not found</h1>")
def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        
        users = Users.objects.filter(email=email).filter(password=password)

        request.session["email"] = email
        request.session["password"] = password
        

        if users:
            return redirect("/ecourse")
        else:
            return redirect("/register")
        
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        global random_gen
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        Users.objects.create(firstname=firstname, lastname=lastname, email=email, password=password).save

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()

        import random

        random_gen = random.randint(100000, 999999)

        body = "Subject: Your password is: " + str(random_gen)

        smtp.login("d08980476@gmail.com", "hpsfddscirizplhz")
        smtp.sendmail("d08980476@gmail.com", email, body)
        
        return redirect("/confirm")
    else:
        return render(request, 'register.html')
    
def confirm(request):
    if request.method == "POST":
        code = request.POST["code"]
        if code == str(random_gen):
            return redirect("/login")
        else:
            return redirect("/confirm")

    return render(request, "confirmation.html")

def logout(request):
    request.session["email"] = ""
    return redirect("/")


# gnfs vizv rsct bcqu