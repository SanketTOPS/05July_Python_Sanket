from django.shortcuts import redirect, render
from .forms import userForm
from .models import userdata

# Create your views here.
def index(request):
    if request.method=='POST':
        user=userForm(request.POST)
        if user.is_valid(): #true
            user.save()
            print("Your data has been saved!")
        else:
            print(user.errors)
    return render(request,'index.html')

def showdata(request):
    data=userdata.objects.all()
    return render(request,'showdata.html',{'data':data})

def deletedata(request,stid):
   id=userdata.objects.get(id=stid)
   userdata.delete(id)
   return redirect('showdata')

def updatedata(request,stid):
    id=userdata.objects.get(id=stid)
    if request.method=='POST':
        updateuser=userForm(request.POST)
        if updateuser.is_valid():
            updateuser=userForm(request.POST,instance=id)
            updateuser.save()
            print("Your records has been updated!")
            return redirect('showdata')
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'stdata':userdata.objects.get(id=stid)})
