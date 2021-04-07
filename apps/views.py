from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from . models import *

# Create your views here.
def home_page(request):
    
    menus = specialty.objects.all()

    salad = salads.objects.all()

    starter = starters.objects.all()

    chef = chefs.objects.all()
    
    context = {'menus': menus, 'salad':salad, 'chef':chef, 'starter':starter}

    return render(request, 'index.html' , context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()


    return render(request, 'contact_form.html')


def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        people = request.POST.get('people')
        message = request.POST.get('message')

        book_for_table = Table( name=name, email=email, 
                                phone=phone, date=date, time=time, 
                                people=people,message=message)

        book_for_table.save()
        messages.success(request,"Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!")
    return render(request, 'table_form.html')