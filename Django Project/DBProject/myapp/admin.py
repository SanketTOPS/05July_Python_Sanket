from django.contrib import admin
from .models import userdata

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=['name','email','city']


admin.site.register(userdata,userAdmin)