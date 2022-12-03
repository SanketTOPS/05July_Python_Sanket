from django.contrib import admin
from .models import studinfo

# Register your models here.

class studAdmin(admin.ModelAdmin):
    list_display=['name','sub','city']

admin.site.register(studinfo,studAdmin)
