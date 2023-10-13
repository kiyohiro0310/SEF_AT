from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", include("SEF.urls")),
    path("admin", include("SEF.urls")),
    path("edit-pet", include("SEF.urls")),
    path("authentication", include("SEF.urls")),
    path("about-us", include("SEF.urls")),
    path("pet-detail", include("SEF.urls")),
    path("pet-form", include("SEF.urls")),
    path("pet-list", include("SEF.urls")),
    path("find-adopter", include("SEF.urls")),
]

urlpatterns += staticfiles_urlpatterns()