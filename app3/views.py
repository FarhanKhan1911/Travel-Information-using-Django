from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'POST':             # To check the request is "POST" or not  
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:

            if User.objects.filter(username=username).exists():  # It is check the following mentioned data is already present in Database or not#
                messages.info(request,"UserName is Already taken......") 
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is Already taken......") # This show the message and also change in html file using jinja 
                return redirect('register')

            else:    
                user = User.objects.create_user(username = username , password = password1, email = email , first_name=first_name,last_name=last_name)
                # It will create the user with this following details #
                user.save();  # It will save it #
                print("user created")
            

        else:
            messages.info(request,"Password is not Matched............")
            return redirect('register')
        return redirect('/')

    else:
        return render (request,"register.html")


def login(request):

    if request.method=='POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
        
            auth.login(request,user)
            return redirect('/')
        
        else:

            messages.info(request,"Invalid Username Or Password...............")
            return redirect("login")

    else:    
        return render (request,'login.html')        


def logout(request):
    auth.logout(request)
    return redirect ('/')        