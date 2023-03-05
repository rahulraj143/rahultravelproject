from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password = request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if login is not None:
             auth.login(request,user)
             return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect(request,'login')
    return render(request,"login.html")
def regist(request):
    if request.method=='POST':
        username=request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email" ]
        password = request.POST["password"]
        cpassword = request.POST["password1"]
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                print("username already taken")
                return redirect("regist")
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"email already taken")
                 print("email already taken")
                 return redirect("regist")
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print("user created")
                return redirect("login")
        else:
            messages.info(request,"password unmatched")
            return redirect("regist")
        return redirect("/")
    return render (request,"regist.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
