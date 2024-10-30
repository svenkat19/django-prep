from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("wELCOME hOME") 
def about(request):
    return HttpResponse("About")