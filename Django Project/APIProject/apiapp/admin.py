from django.contrib import admin
from .models import userinfo

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=['name','sub','city']

admin.site.register(userinfo,userAdmin)