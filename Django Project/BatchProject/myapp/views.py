from django.shortcuts import render,redirect
from .forms import usersignupForm,notesForm,updateForm
from .models import userSignup
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from BatchProject import settings
import random
import requests


# Create your views here.

def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup':
            username=""
            newuser=usersignupForm(request.POST)
            if newuser.is_valid():
                username=newuser.cleaned_data.get("username")
                try:
                    un=userSignup.objects.get(username=username)
                    print("Username is already exists!")
                    messages.error(request,"Username is already exists!")
                except userSignup.DoesNotExist:
                    newuser.save()
                    print("Signup successfully!")

                    # Email Sending
                    otp=random.randint(1111,9999)
                    sub='Welcome!'
                    msg=f'Hello User!\nWelcome to NotesApp\n\nYour account has been created with us.\nEnjoy our services.\nYour one time password: {otp}\nNeed any help...\n+91 9724799469 | sanket.tops@gmail.com'
                    from_ID=settings.EMAIL_HOST_USER
                    to_ID=['manavgathani@gmail.com','paraspethani12@gmail.com','dishabaldha99@gmail.com','pansuriyajenisha999@gmail.com','romil.pathak18@gmail.com','zvirbhadrasinh7@gmail.com']
                    #to_ID=[request.POST['username']]
                    send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
                    
                    messages.info(request,"Signup successfully!")
                    return redirect('notes')
            else:
                print(newuser.errors)
                messages.error(request,"Error! Something wen wrong...Try after some time.")
        elif request.POST.get('signin')=='signin':
            unm=request.POST['username']
            pas=request.POST['password']

            user=userSignup.objects.filter(username=unm,password=pas)
            uid=userSignup.objects.get(username=unm)
            print("Username:",uid)
            print("UserID:",uid.id)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm #session creation
                request.session['uid']=uid.id

                # SMS Sending
                otp=random.randint(1111,9999)
                url = "https://www.fast2sms.com/dev/bulkV2"
                #querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","variables_values":f"{otp}","route":"otp","numbers":"9429369656,7435834716,7285068225,6353894918,8758169039,9727717779"}
                querystring = {"authorization":"PSqGhvu5BkQv1WEvvWH6PIgV0vr1IcOIEzgsN1fZMHFG0WJapJ1hGGIwYfq8","message":f"Dear User\nWelcome to NotesApp\nYour one time password {otp}","language":"english","route":"q","numbers":"9429369656,7435834716"}
                headers = {
                    'cache-control': "no-cache"
                }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
                return redirect('notes')
            else:
                print("Error! Username or Password does not match.") 
                messages.error(request,"Error! Username or Password does not match.")   
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        mynote=notesForm(request.POST,request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been submitted!")
        else:
            print(mynote.errors)
    return render(request,'notes.html',{'cuser':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cid=userSignup.objects.get(id=uid)
    if request.method=='POST':
        updatefrm=updateForm(request.POST)
        if updatefrm.is_valid():
            updatefrm=updateForm(request.POST,instance=cid)
            updatefrm.save()
            print("Your profile has been updated!")
            return redirect('notes')
        else:
            print(updatefrm.errors)
    return render(request,'profile.html',{'cid':userSignup.objects.get(id=uid),'cuser':user})

def userlogout(request):
    logout(request)
    return redirect("/")
