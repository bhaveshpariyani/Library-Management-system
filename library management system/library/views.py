from django.shortcuts import render, redirect
from .models import Books
from .forms import BooksForms
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
# from django.contrib.auth import 
from django.contrib.auth.decorators import login_required


def delete_book(request,book_id):
    Book = Books.objects.get(pk=book_id)
    Book.delete()
    return redirect("books_list")

def update_book(request,book_id):
    Book = Books.objects.get(pk=book_id)
    form = BooksForms(request.POST or None,instance=Book)
    if form.is_valid():
            form.save()
            return redirect("books_list")
    return render(request,'update_book.html',{'book':Book,'form':form})


def show_book(request,book_id):
    Book = Books.objects.get(pk=book_id)
    return render(request,'show_book.html',{'book':Book})

def books_list(request):
    Books_list = Books.objects.all()

    p = Paginator(Books.objects.all(),20)
    page = request.GET.get('page')
    Book = p.get_page(page)
    pages = "a" * Book.paginator.num_pages


    return render(request,"Books_list.html",{'Books_list':Books_list,'Book':Book,"pages":pages})

def add_books(request):
    submitted = False

    if request.method == "POST":
        form = BooksForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_books?submitted=True')
    else:
        form = BooksForms
        if 'submitted' in request.GET:
            submitted = True
    return render(request,"add_books.html",{'form':form,'submitted':submitted})

def home(request):
    return render(request,'home.html',{})