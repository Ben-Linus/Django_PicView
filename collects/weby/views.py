from django.shortcuts import render, redirect
from django.http import HttpResponse
from weby.models import Image, Category


# Create your views here.

def aboutus(request):
    name = 'Ben'
    gender = 'Male'
    return render(request, "weby/about.html", {
        'name': name,
        'gender' : gender
    })

def show_home_page(request):
    cats = Category.objects.all()
    images= Image.objects.all()
    data={
        'images': images,
        'cats': cats
    }

    return render(request, "weby/home.html", data )

def show_category_page(request,cid):
    cats = Category.objects.all()
    category=Category.objects.get(pk=cid)
    images= Image.objects.filter(cat=category)
    data={
        'images': images,
        'cats': cats
    }
    
    return render(request, "weby/home.html", data)

def home(request):
    return redirect('')