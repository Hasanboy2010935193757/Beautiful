from django.shortcuts import render
from .models import Maxsulot, Rasm, Haridor


# Create your views here.

def index(request):
    maxsulot = Maxsulot.objects.all()
    rasm = Rasm.objects.all()
    haridor = Haridor.objects.all()

    context = {
        'maxsulot': maxsulot,
        'rasm': rasm,
        'haridor': haridor

    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request,'about.html',context={})


def client(request):
    return render(request,'client.html',context={})

def contact(request):
    return render(request,'contact.html',context={})

def products(request):
    maxsulot = Maxsulot.objects.all()

    contact = {
        'maxsulot': maxsulot,

    }
    return render(request, 'products.html', context=contact)


def detail(request, pk):
    products = Maxsulot.objects.get(id=pk)

    contact = {
        'products': products,

    }
    return render(request, 'detail.html', context=contact)