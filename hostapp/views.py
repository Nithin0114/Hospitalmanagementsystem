from django.shortcuts import render
from . models import Departments,Doctors,Contact
from .forms import BookingForm 

# Create your views here.
def home(request):
    return render(request,'home.html')
def education(request):
    return render(request,'education.html')
def doctors(request):
    dict_docs={
        'doctors': Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def departments(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dept)
def contact(request):
    dict_contact={
        'contactkey':Contact.objects.all()
    }
    return render(request,'contact.html',dict_contact)

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm
    dict_form={
        'form':form
    }
    return render(request,"booking.html",dict_form)
def about(request):
    return render(request,'about.html')