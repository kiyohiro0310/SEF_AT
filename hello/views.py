import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django.")

def hello_there(request):
    # print(request.build_absolute.uri())
    return render(
        request,
        'home.html',
    )