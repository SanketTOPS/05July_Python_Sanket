from django.shortcuts import render
from .models import studinfo
from django.db.models import Q



# Create your views here.

def index(request):
    search_post = request.GET.get('search')
    #stdata=studinfo.objects.all()
    if search_post:
        stdata = studinfo.objects.filter(Q(name__icontains=search_post) & Q(sub__icontains=search_post))
        print(stdata)
        print("Search found......")
    else:
        # If not searched, return default posts
        stdata = studinfo.objects.all().order_by("-date_created")
        print("Error!")
    return render(request,'index.html',{'stdata':stdata})