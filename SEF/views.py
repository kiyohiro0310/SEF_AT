import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(
        request,
        'home.html',
    )

# Pet list
def admin(request):
    return render(
        request,
        'admin.html'
    )


def authentication(request):
    return render(
        request,
        'authentication.html'
    )

def about_us(request):
    return render(
        request,
        "about-us.html"
    )

def pet_detail(request):
    return render(
        request,
        'pet-detail.html'
    )

def pet_form(request):
    return render(
        request,
        'pet-form.html'
    )

def pet_list(request):
    return render(
        request,
        'pet-list.html'
    )