import re
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def index_view(request):
    return render(request,'landing/eBusiness/index.html')

@csrf_exempt
def bussiness_base(request):
    user = request.user
    # pk  = int(request.COOKIES['pkb']) # make sure to delete when loging out
    # user = User.objects.get(id=pk)
    print("usewwwwwwwwwwwwwwwwwwwwwwwwwwr"+user.username)
    # displays the portforlio
    return render(request,"bussiness/Home/sb-admin-2-bootstrap-4/index.html",{'user':user})

def bussiness_signup(request):
    userForm=UserForm()
    bussinessForm=BussinessForm()
    mydict={'userForm':userForm,'bussinessForm':bussinessForm}
    if request.method=='POST':
        userForm=UserForm(request.POST)
        bussinessForm=BussinessForm(request.POST,request.FILES)
        if userForm.is_valid() and bussinessForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=bussinessForm.save(commit=False)
            customer.user=user
            customer.save()
            my_bussiness_group = Group.objects.get_or_create(name='bussiness')
            my_bussiness_group[0].user_set.add(user)

            return HttpResponseRedirect("bussiness_signin")

        else:
            HttpResponse("error")
    return render(request,"bussiness/signup/signup.html",{'userForm':userForm,'bussinessForm':bussinessForm})
@csrf_exempt
def bussiness_signin(request):
    userForm=UserForm()
    if request.method == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(
    		    request, 
    		    username=username, 
    		    password=password
        )
        login(request, user)
        return redirect('bussiness_base/',user='user')
        # if user:
        #     login(request, user)
        #     print("signingccccccccccccccccccccccccccccccccccs in",user)
        #     return redirect('bussiness_base',user='user')
        # else:
          #     return HttpResponse("Invalid credentials.")
        
            
    # userForm=UserForm()
    # if request.method=='POST':
    #     userForm=UserForm(request.POST)
    #     user = authenticate(username=request.POST['username'],password=request.POST['password'])
    #     if user is not None:
    #         id= user.id
    #         user = User.objects.get(id=id)
    #         print(id)
    #         response = HttpResponseRedirect("bussiness_base/"+user)
    #         response.set_cookie('pkb',id)
    #         return response
    #     else:
    #         HttpResponse("error") 
    return render(request,"bussiness/signin/login.html",{'userForm':userForm})

def customer_home(request):
    # print(pk)
    # pk  = int(request.COOKIES['pk']) # make sure to delete when loging out
    # user = User.objects.get(id=pk)
    # print(user.email)
    user = request.user
    return render(request,"customer/home/eshopper-1.0.0/index.html",{'user':user})

def customer_signup(request):
    userForm=UserForm()
    customerForm=CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=UserForm(request.POST)
        customerForm=CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='customer')
            my_customer_group[0].user_set.add(user)

            return HttpResponseRedirect("customer_signin")

        else:
            HttpResponse("error")

    return render(request,"customer/registration/sign up/signup.html",{'userForm':userForm,'customerForm':customerForm})
from django.contrib.auth import authenticate

@csrf_exempt
def customer_signin(request):
    userForm=UserForm()
    if request.method == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(
    		    request, 
    		    username=username, 
    		    password=password
        )
        login(request, user)
        return redirect('customer_home/',user='user')
    # userForm=UserForm()
    # if request.method=='POST':
    #     userForm=UserForm(request.POST)
    #     user = authenticate(username=request.POST['username'],password=request.POST['password'])
    #     if user is not None:
    #         id= user.id
    #         user = User.objects.get(id=id)
    #         print(id)
    #         response = HttpResponseRedirect("customer_home/")
    #         # response.delete_cookie('user')
    #         response.set_cookie('pk',id)
    #         return response
    #     else:
    #         HttpResponse("error")   
   
        # No backend authenticated the credentials    
    return render(request,"customer/registration/login/login.html",{'userForm':userForm})

def customer_profile(request):
    return render(request,"",{})

def events_home(request):
    # display brief info of events around the customer
    return render(request,"",{})

def event_detail(request):
    # display one event with all the neccesary info
    return render(request,"",{})

def news_home(request):
    return render(request,"news/Magz-master/index.html",{})

def news_detail(request):
    return render(request,"news/Magz-master/single.html",{})

def expertise_portforlio(request):
    return render(request,"Expertise/portforlio/iPortfolio/index.html",{})

def expertise_base(request):
    # pk  = int(request.COOKIES['pk']) # make sure to delete when loging out
    # user = User.objects.get(id=pk)
    # print(user.email)
    user = request.user
    return render(request,"bussiness/Home/sb-admin-2-bootstrap-4/index.html",{'user':user})

def expertise_signup(request):
    userForm=UserForm()
    expertForm=ExpertForm()
    mydict={'userForm':userForm,'expertForm':expertForm}
    if request.method=='POST':
        userForm=UserForm(request.POST)
        expertForm=ExpertForm(request.POST,request.FILES)
        if userForm.is_valid() and expertForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            expert=expertForm.save(commit=False)
            expert.user=user
            expert.save()
            my_expert_group = Group.objects.get_or_create(name='expert')
            my_expert_group[0].user_set.add(user)

            return HttpResponseRedirect("expertise_signin/")

        else:
            HttpResponse("error")
    return render(request,"Expertise/registration/sign up/signup.html",{'userForm':userForm,'expertForm':expertForm})

@csrf_exempt
def expertise_signin(request):
    userForm=UserForm()
    if request.method == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(
    		    request, 
    		    username=username, 
    		    password=password
        )
        login(request, user)
        return redirect('expertise_base/',user='user')
    # userForm=UserForm()
    # if request.method=='POST':
    #     userForm=UserForm(request.POST)
    #     user = authenticate(username=request.POST['username'],password=request.POST['password'])
    #     if user is not None:
    #         id= user.id
    #         user = User.objects.get(id=id)
    #         print(id)
    #         response = HttpResponseRedirect("expertise_base/")
    #         # response.delete_cookie('user')
    #         response.set_cookie('pk',id)
    #         return response
    #     else:
    #         HttpResponse("error") 
    return render(request,"Expertise/registration/login/login.html",{'userForm':userForm})

def logout(request):
    return render(request,"landing/eBusiness/index.html",{})






