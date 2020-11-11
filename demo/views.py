from django.contrib.auth import logout
from django.http import HttpResponse

from django.shortcuts import render

from django.contrib import messages

from django.shortcuts import HttpResponseRedirect


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')


def index(req):
    print("ovo je log neki")
    return render(req, "demo/home.html")


def template(req):
    messages.add_message(req, messages.INFO, 'Ovo je poruka neka...')
    data = {"name": "janko diminic"}
    return render(req, "demo/index.html", data)


def adminlte(req):
    return render(req, "adminlte.html")
