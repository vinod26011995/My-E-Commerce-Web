from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import *



# Create your views here.

class Login(View):

    def get(self,request):
        return render(request,'login.html')


    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password,'both data')
        if username and password:
            print('line 21')
            check = UserModel.objects.filter(username=username,password=password)
            if check:
                print('dfghj')
                return redirect('home')
        return render(request,'login.html')
    
class Register(View):
    def get(self,request):


        return render (request,'register.html')
    

    def post(self,request):
        Email = request.POST.get('email')
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        print('hello',Email,Username,Password)
        crt=UserModel.objects.create(email=Email,username=Username,password=Password)
        print(crt,'data')
        if crt:
            return redirect('login')
        return render(request,'register.html')
    
class index(View):
    def get(self,request):
        return render(request,'home.html')

