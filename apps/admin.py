from django.contrib import admin
from . models import *
# Register your models here.

class specialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

class startersAdmin(admin.ModelAdmin):
    list_display = ('name','price')


class saladsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class chefsAdmin(admin.ModelAdmin):
    list_display = ('name','title')


class ContactAdmin(admin.ModelAdmin):
    list_display =  ('name','email','subject','message','date')




admin.site.register(Table)
admin.site.register(Contact, ContactAdmin)
admin.site.register(chefs, chefsAdmin)
admin.site.register(specialty,  specialtyAdmin)
admin.site.register(starters, startersAdmin)
admin.site.register(salads, saladsAdmin)