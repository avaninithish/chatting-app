from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from login import urls

# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def registerdisp(request):
    return render(request,'registerdisp.html') 
def logindisp(request):
    return render(request,'logindisp.html')
def register(request):
    if request.method == "POST":
        username=request.POST['username']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

 
        if password1 == password2:
            if  User.objects.filter(username=username).exists():
                messages.info(request,'user already exist')
                return redirect('registerdisp')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('registerdisp')
            else:
                users = User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password1,email=email)
                users.save()
                print("user created")
                return redirect('logdisp')

        else:
            messages.info(request,'password is not matching')
            return redirect('registerdisp')
        
    else:
        return render(request,'registerdisp.html')

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'No user name or password')
            return redirect('logdisp')
    else:
         return redirect('logdisp')

def logout(request):
    auth.logout (request)
    return redirect('welcome')
