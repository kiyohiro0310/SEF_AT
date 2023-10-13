
import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from SEF.forms import UserForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout

from SEF.models import Pet, User

# Create your views here.
def home(request):
    pets = Pet.objects.all().order_by("-date_added").values()[:20]
    return render(
        request,
        'home.html',
        context={'pets': pets}
    )

# Search pet from hero section
def search_pet(request):
    pets = []
    category = 'All'
    if request.method == "POST":
        try:
            if request.POST:
                species = request.POST["species"].title()
                age = request.POST["age"]
                age_range= ''
                if age == '5':
                    age_range = [0,5]
                    age = "0~5 Years Old"
                if age == '6-9':
                    age_range = [6,9]
                    age = "6~9 Years Old"
                if age == '10':
                    age_range = [10,100]
                    age = "10~ Years Old"
                state = request.POST["state"]
                category = f"Category: {species}, {age}, {state}"

                pets = Pet.objects.all().filter(species=species, age__range=age_range, state=state).order_by("-date_added").values()
            else:
                pets = Pet.objects.all().order_by("-date_added").values()

            return render(
                request,
                'pet-list.html',
                context={
                    'pets': pets,
                    'category': category
                    }
                )
        except:
            pets = Pet.objects.all().order_by("-date_added").values()
            return render(
                request,
                'pet-list.html',
                context={
                    'pets': pets,
                    'category': f"Category: {category}",
                    'error_msg': "Invalid search, please select all options."
                    }
                )
    else:
        pets = Pet.objects.all().order_by("-date_added").values()
        return render(
            request,
            'pet-list.html',
            context={'pets': pets}
            )

def admin(request):
    pets = []
    category = 'All'
    if request.method == "POST":
        try:
            if request.POST:
                species = request.POST["species"].title()
                age = request.POST["age"]
                age_range= ''
                if age == '5':
                    age_range = [0,5]
                    age = "0~5 Years Old"
                if age == '6-9':
                    age_range = [6,9]
                    age = "6~9 Years Old"
                if age == '10':
                    age_range = [10,100]
                    age = "10~ Years Old"
                state = request.POST["state"]
                category = f"Category: {species}, {age}, {state}"

                pets = Pet.objects.all().filter(species=species, age__range=age_range, state=state).order_by("-date_added").values()
            else:
                pets = Pet.objects.all().order_by("-date_added").values()

            return render(
                request,
                'admin.html',
                context={
                    'pets': pets,
                    'category': category
                    }
                )
        except:
            pets = Pet.objects.all().order_by("-date_added").values()
            return render(
                request,
                'admin.html',
                context={
                    'pets': pets,
                    'category': f"Category: {category}",
                    'error_msg': "Invalid search, please select all options."
                    }
                )
    else:
        pets = Pet.objects.all().order_by("-date_added").values()
        return render(
            request,
            'admin.html',
            context={'pets': pets}
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
    pets = []
    category = 'All'
    try:
        if 'specie' in request.GET:
            pets = Pet.objects.all().filter(species=request.GET["specie"].title()).order_by("-date_added").values()
            category = request.GET["specie"].title()
        elif 'state' in request.GET:
            pets = Pet.objects.all().filter(state=request.GET["state"].upper()).order_by("-date_added").values()
            category = request.GET["state"].upper()
        elif 'gender' in request.GET:
            pets = Pet.objects.all().filter(gender=request.GET["gender"].title()).order_by("-date_added").values()
            category = request.GET["gender"].title()
        elif 'age' in request.GET:
            if request.GET['age'] == '5':
                pets = Pet.objects.all().filter(age__range=[0, 5]).order_by("-date_added").values()
                category = "0~5 Years Old"
            elif request.GET['age'] == '6-9':
                pets = Pet.objects.all().filter(age__range=[6, 9]).order_by("-date_added").values()
                category = "6~9 Years Old"
            elif request.GET['age'] == '10':
                pets = Pet.objects.all().filter(age__range=[10, 100]).order_by("-date_added").values()
                category = "10~ Years Old"
        else:
            pets = Pet.objects.all().order_by("-date_added").values()


        return render(
            request,
            'pet-list.html',
            context={
                'pets': pets,
                'category': f"Category: {category}"
            }
        )
    except:
        pets = Pet.objects.all().order_by("-date_added").values()

        return render(
            request,
            'pet-list.html',
            context={
                'pets': pets,
                'category': f"Category: {category}"
            }
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

def edit_pet(request):
    pet_id = request.GET["pet_id"]
    print(pet_id)
    return redirect("/admin")

def delete_pet(request):
    pet_id = request.GET["pet_id"]
    print(pet_id)
    return redirect("/admin")
