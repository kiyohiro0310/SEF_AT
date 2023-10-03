from django.urls import path
from SEF import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin", views.admin),
    path("authentication", views.authentication),
    path("about-us", views.about_us),
    path("pet-detail", views.pet_detail),
    path("pet-form", views.pet_form),
    path("pet-list", views.pet_list)
]