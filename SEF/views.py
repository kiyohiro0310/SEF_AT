
import datetime
from email.mime import application
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
                state = request.POST["state"]
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

                category = f"Category: {species}, {age}, {state}"

                if species == "Others":
                    pets = Pet.objects.all().filter(age__range=age_range, state=state).exclude(species='Dog').exclude(species='Cat').order_by("-date_added").values()
                else:
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
                state = request.POST["state"]
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

                category = f"Category: {species}, {age}, {state}"

                if species == "Others":
                    pets = Pet.objects.all().filter(age__range=age_range, state=state).exclude(species='Dog').exclude(species='Cat').order_by("-date_added").values()
                else:
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

        try:
            if request.GET["page"] == "pets":
                return render(
                    request,
                    'admin.html',
                    context={
                        'pets': pets,
                        'pets_content': True
                    }
                )
            elif request.GET["page"] == "applications":
                applications = []
                return render(
                    request,
                    'admin.html',
                    context={
                        "admin_app_page": True,
                        "applications": applications
                    }
                )
            else:
                return render(
                    request,
                    'admin.html',
                    context={
                        'pets': pets,
                        'pets_content': True
                    }
                )
        except:
            return render(
                request,
                'admin.html',
                context={
                    'pets': pets,
                    "pets_content": True
                    }
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
            if request.GET["specie"].title() == "Others":
                pets = Pet.objects.all().exclude(species='Dog').exclude(species='Cat').order_by("-date_added").values()
            else:
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
    if request.method == 'GET':
        pet_id = request.GET["pet_id"]
        pet = Pet.objects.get(id=pet_id)

        return render(
            request,
            'pet-edit.html',
            context={
                "pet": pet
            }
        )

    if request.method == "POST":
        pets = Pet.objects.all().order_by("-date_added").values()
        try:
            pet_id = request.POST["pet-id"]
            pet_name = request.POST["pet-name"]
            species = request.POST["species"].title()
            breed = request.POST["breed"]
            age = request.POST["age"].title()
            gender = request.POST["gender"].title()
            status = request.POST["status"]
            suburb = request.POST["suburb"].title()
            state = request.POST["state"].upper()
            fee = request.POST["fee"]
            description = request.POST['description']

            pet = Pet.objects.get(id=pet_id)
            pet.name = pet_name
            pet.species = species
            pet.breed = breed
            pet.age = age
            pet.gender = gender
            pet.status = status
            pet.suburb = suburb
            pet.state = state
            pet.fee = fee
            pet.description = description

            pet.save()

            return render(
                request,
                'admin.html',
                context={
                    'pets': pets,
                    'category': "All",
                    'pets_content': True,
                    'edit_success': f"Successfully editted pet: {pet_id}"
                    }
                )

        except:
            return render(
                request,
                'admin.html',
                context={
                    'pets': pets,
                    'category': "All",
                    'pets_content': True,
                    'edit_fail': "Edit failed"
                    }
                )

def delete_pet(request):
    pet_id = request.GET["pet_id"]
    pet = Pet.objects.get(id=pet_id)
    pet.delete()

    pets = Pet.objects.all().order_by("-date_added").values()
    return render(
                request,
                'admin.html',
                context={
                    'pets': pets,
                    'category': "All",
                    'pets_content': True,
                    'delete': f"Successfully deleted pet: {pet_id}"
                    }
                )


def find_adopter(request):
    current_date = datetime.datetime.now()
    if request.method == "POST":
        try:
            image_path = request.POST["image_path"]
            pet_name = request.POST["pet-name"]
            species = request.POST["species"].title()
            breed = request.POST["breed"]
            age = request.POST["age"].title()
            gender = request.POST["gender"].title()
            status = request.POST["status"]
            suburb = request.POST["suburb"].title()
            state = request.POST["state"].upper()
            fee = request.POST["fee"]
            description = request.POST['description']
            date_added = current_date.strftime('%Y-%m-%d %H:%M:%S')

            new_pet = Pet(
                image_path=image_path,
                name=pet_name,
                species=species,
                breed=breed,
                age=age,
                gender=gender,
                status=status,
                suburb=suburb,
                state=state,
                fee=fee,
                description=description,
                date_added=date_added
            )

            new_pet.save()

            return redirect("/pet-list")

        except:
            return redirect("/pet-list")

    return render(
        request,
        'find-adopter.html'
    )