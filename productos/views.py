from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'index.html')

def login (request):
    return render(request,'login.html')

def list_products(request):
    return render(request,'producto/lis_products.html')