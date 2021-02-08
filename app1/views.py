from django.shortcuts import render,HttpResponse

# Create your views here.
def hello(request):
    # return HttpResponse("Hello, world. 96ebb3a7 is the polls index.")
    # return render (request,'home.html')           
    return render (request,'base.html',{'name':'Farhan'})        

def add(request):

    # val1 = request.GET['num1']
    # val2 = request.GET['num2']  #----------This code adding string and When we use "GET" so it show the entering data 
    # res = val1 + val2           # into the url of the browser ---------------------------

    val1 = int(request.POST["num1"])   #----------This code adding integer and When we use "POST" so it does not show the entering data 
    val2 = int(request.POST["num2"])   # into the url of the browser ---------------------------
    res = val1 + val2

    return render (request,"result.html",{'result':res})    