from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import Contact,Product
from django.views import View





# Create your views here.
@login_required(login_url="login")
def home(request):
    return render(request,"home.html")

def userlogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("password")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('login')
    return render(request,'login.html')


def register(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        
        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/register')


        try:
            if User.objects.get(username=uname):
                messages.info(request,"UserName Is Taken")
                return redirect('/register')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email Is Taken")
                return redirect('/register')
        except:
            pass
    
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"Signup Successfull")
        return redirect('login')
              
    return render(request,'register.html')


def userlogout(request):
    logout(request)
    messages.info(request,"logout successfull")
    return redirect('login')

@login_required(login_url='login')
def contact(request):
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        query=Contact(name=fname,email=femail,phoneNumber=phone,description=desc)
        query.save()
        messages.info(request,"Thanks For Reaching Us! We will get back you soon....")
        return redirect('contact')
    return render(request,'contact.html')


class category(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        return render(request,"category.html",locals())

class productdetails(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"productdetails.html",locals())
