from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.
def index(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
        }
    return render(request, 'index.html' , context)

def register(request):
    if request.method=="POST":
        Book.objects.create(title=request.POST['title'],desc=request.POST['description'])
        

    
    return redirect('/')



def index2(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all(),
        }
    return render(request, 'book.html' , context)

def display(request,id1):
    book = Book.objects.get(id =id1)
    context={
        "books":book,
        "authors":Author.objects.all()
    }
    
    return render(request, 'book.html' , context)


def add(request,id1):
    book = Book.objects.get(id =id1)
    context = {
           "books":Book.objects.all(),
           "authors":Author.objects.all()
    }
    return render(request,'book.html',context)
   