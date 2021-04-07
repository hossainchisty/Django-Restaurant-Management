from django.shortcuts import render
from datetime import datetime
from . models import *

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()


    menus = specialty.objects.all()

    salad = salads.objects.all()

    starter = starters.objects.all()

    chef = chefs.objects.all()
    
    context = {'menus': menus, 'salad':salad, 'chef':chef, 'starter':starter}

    return render(request, 'index.html' , context)

