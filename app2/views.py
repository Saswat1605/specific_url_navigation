from django.shortcuts import render

# Create your views here.
def shoe(request):
    return render (request,'shoe.html')