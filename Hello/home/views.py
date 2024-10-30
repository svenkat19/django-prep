from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("wELCOME hOME")
    context={
        "var":"this is a variable"
    } 
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def services(request):
    return HttpResponse("Servicessss")
def contact(request):
    return HttpResponse("contact")