import datetime
from django.http import HttpResponse
from django.shortcuts import render

from SEF.models import Pet

# Create your views here.
def home(request):
    pets = Pet.objects.all().order_by("-id").values()
    return render(
        request,
        'home.html',
        context={'pets': pets}
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
    pet_id = request.GET["pet_id"]
    pet = Pet.objects.get(id=pet_id)
    print(pet)
    return render(
        request,
        'pet-detail.html',
        context={'pet': pet}
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