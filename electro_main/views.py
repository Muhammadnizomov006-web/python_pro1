from multiprocessing import context
from os import name

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render,redirect
from django.template.context_processors import request
from django.views.generic import DetailView, View, CreateView

from electro_main.models import *

# Create your views here.

def Get_context():
    return {
        "product": Product.objects.all(),
        "category": Catigorya.objects.all(),
    }



class Detalles(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

@login_required
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

login_required(login_url='/login/')
def Search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(Q(name__icontains=query))
    # products1 = Product.objects.get(id=id)
    return render(request, 'search.html', {'products': products, 'query': query})








class Login(View):
    def get(self,request):
        return render(request, 'login.html')



    def post(self,request):
        usernmae=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        user=authenticate(request=request,usernmae=usernmae, password=password,email=email)
        if user is not None:
            login(request,user)
            return redirect('index.html')
        return render(request, 'index.html',{'error':"Hato kitildi "})






# def Registers(request):
#     if request.method == "POST":
#         form =UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/otdi/')
#     form = UserCreationForm()
#     return render(request,'registration/Loginlar.html',{'form':form})
#

class Register(CreateView):
    form_class = UserCreationForm
    template_name = "Register.html"
    success_url = ',/Register.html/'





















def Qidiruv(requset):
    izlash=requset.GET.get('s','')
    product=Product.objects.filter(Q(name__icontains=izlash))

    return render(requset,'tek.html',{'product':product,'sorov':izlash})
