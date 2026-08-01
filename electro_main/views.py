from multiprocessing import context
from os import name

from django.db.models import Q
from django.shortcuts import render,redirect
from django.views.generic import DetailView

from electro_main.models import *

# Create your views here.

def Get_context():
    return {
        "product": Product.objects.all(),
        "category": Catigorya.objects.all(),
    }



class Detalles(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


def index(request):
    context=Get_context()
    return render(request, 'index.html', context)




def checkout(request):
    return render(request, 'checkout.html')




def blank(request):
    return render(request, 'blank.html')





def product(request):
    context= Get_context()
    return render(request, 'product.html',context)





def store(request):
    return render(request, 'store.html')

def Biling(request):
    if request.method == "POST":
        last_name=request.POST['last_name']
        first_name=request.POST['first_name']
        email=request.POST['email']
        adres=request.POST['adres']
        sity=request.POST['sity']
        country=request.POST['country']
        zip_code=request.POST['zip_code']
        telephone=request.POST['telephone']
        acca=request.POST['acca']
        password=request.POST['password']
        Checkout.objects.create(last_name=last_name,first_name=first_name,email=email,\
                                adres=adres,sity=sity,country=country,zip_code=zip_code,\
                                telephone=telephone,accc=acca,password=password)
        return   redirect('/index/')



def Taj(request):
    tek_con={
        'taj_contex':Tek.objects.all(),
    }
    return render(request, 'tek.html',tek_con)


def Search(request):
    query = request.GET.get('q', '')

    products = Product.objects.filter(Q(name__icontains=query))
    # products1 = Product.objects.get(id=id)
    return render(request, 'search.html', {'products': products, 'query': query})

























def Qidiruv(requset):
    izlash=requset.GET.get('s','')
    product=Product.objects.filter(Q(name__icontains=izlash))

    return render(requset,'tek.html',{'product':product,'sorov':izlash})
