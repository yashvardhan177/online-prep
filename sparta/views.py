from django.shortcuts import render,HttpResponse
from datetime import datetime
from  sparta.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"yash first django practice webpage"
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is sparta")
def About (request):
    return render(request, 'About.html')

def Services(request):
    return render(request, 'Services.html')

def contact(request):
    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(email=email,password=password,date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent.')
    return render(request, 'Contact.html')

 #return HttpResponse("this is about page")
