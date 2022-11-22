from django.shortcuts import redirect, render

from myapp.models import signup_master
from .forms import signupForm
from django.contrib.auth import logout

# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['email']
        pas=request.POST['password']
        user=signup_master.objects.filter(email=unm,password=pas)
        if user: #true
            print("Login Successfully!")
            request.session['user']=unm
            return redirect('home')
        else:
            print("Error...Login fail!")
    return render(request,'index.html')

def usersignup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect('home')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')

def home(request):
    cuser=request.session.get('user')
    return render(request,'home.html',{'user':cuser})

def userlogout(request):
    logout(request)
    return redirect("/")
