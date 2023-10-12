from django.urls import path
from SEF import views
from django.contrib import admin

urlpatterns = [
    path("", views.home, name="home"),
    path("admin", views.admin),
    path("authentication", views.authentication),
    path("about-us", views.about_us),
    path("pet-detail", views.pet_detail),
    path("pet-form", views.pet_form),
    path("pet-list", views.pet_list),
    path("signup", views.signup, name="signup"),
    path("login", views.login_view, name="login"),
    path("logout", views.signout),
    path("search-pet", views.search_pet),
    path("edit-pet", views.edit_pet),
    path("delete-pet", views.delete_pet)
]