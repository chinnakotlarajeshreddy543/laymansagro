from django.contrib import admin
from formApp.models import Practice,Products

class Practiceadmin(admin.ModelAdmin):
    list_display=['name','roll','branch','college']

admin.site.register(Practice,Practiceadmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display=['pname','pno','pdetails','paddr']

admin.site.register(Products,ProductsAdmin)

# Register your models here.
