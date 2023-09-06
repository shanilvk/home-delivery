from django.shortcuts import render,redirect
from account.models import Contact
from django.http import HttpResponse
from .forms import createuser,signinform
from django.views.generic import View
from django.contrib import messages
from items.models import foods

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact_us(request):
    context={}
    if request.method=="POST":
        name= request.POST.get("name")
        sub= request.POST.get("subject")
        msz= request.POST.get("message")
        
        obj= Contact.objects.get(name=name, subject=sub, message=msz)
        obj.save()
        context['message']=f"Dear {name},Thanks for your time!"
        
    return render(request,'contact.html',context)



def about(request):
    return render(request,'about.html')
def booking(request):
    return render(request,'booking.html')


def menu(request):
    
    return render(request,"menu.html")


def vegetarian(request):
    
    vegs=foods.objects.filter(category='vegetarian')
    context={'vegs':vegs}
    return render(request,'veg.html',context)



def nonvegetarian(request):
    
    nonvegs=foods.objects.filter(category='nonveg')
    context={'nonveg':nonvegs}
    return render(request,'nonveg.html',context)



def beverage(request):
    
    bev=foods.objects.filter(category='beverage')
    context={'bev':bev}
    return render(request,'beve.html',context)



class signupview(View):
    
    def get(self,request):
        suform=createuser()
        return render(request,'signup.html',{'su':suform})
    def post(self,request):
        form_data=createuser(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"you are successfully registerd!!!!!!")
            return redirect('signin')
        
        else:
            messages.error(request,'invalid input')
            return redirect('signup')
        
        
        
class signinview(View):
    def get(self,request):
        siform=signinform()
        return render(request,'signin.html',{'si':siform})
    def post(self,request):
        form_data=signinform(data=request.POST)
        if form_data.is_valid():
            
            messages.success(request,'login success!!!')
            return redirect('index')
        
        else:
            messages.error(request,'invalid input')
            return redirect('index')