from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.

def index(req):
    print("ovo je log neki")
    return render(req, "demo/home.html")


def template(req):
    data = {"name": "janko diminic"}
    return render(req, "demo/index.html", data)
