
import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from SEF.forms import UserForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout

from SEF.models import Pet, User

# Create your views here.
def home(request):
    pets = Pet.objects.all().order_by("-id").values()[:20]
    return render(
        request,
        'home.html',
        context={'pets': pets}
    )

def admin(request):
    return render(
        request,
        'admin.html'
    )

def authentication(request):
    method = request.GET["auth_method"]
    return render(
        request,
        'authentication.html',
        context={'auth_method': method}
    )

def about_us(request):
    return render(
        request,
        "about-us.html"
    )

def pet_detail(request):
    pet_id = request.GET["pet_id"]
    pet = Pet.objects.get(id=pet_id)
    print(pet.description)
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
    pets = pets = Pet.objects.all().order_by("-id").values()
    return render(
        request,
        'pet-list.html',
        context={'pets': pets}
    )

def signup(request):
    form = UserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            user.password = make_password(user.password)
            user.last_login = datetime.date.today()
            user.save()

            request.session['login_user'] = user.id

        return redirect("/")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.get(username=username)

        if user is not None and check_password(password, user.password):
            request.session['login_user'] = user.id
            return redirect("/")

        return redirect("/authentication?auth_method=login")

def signout(request):
    del request.session['login_user']
    return redirect("/")



