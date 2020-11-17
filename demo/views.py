import datetime
from datetime import timezone

from background_task.models import Task, CompletedTask
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, request

from logging import getLogger

from django.shortcuts import render

from django.contrib import messages

from django.shortcuts import HttpResponseRedirect

from demo import my_task

log = getLogger(__name__)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                print('User not found')
        else:
            print(form.errors)
            return render(request, 'adminlte/login.html', {'form': form})

    return render(request, 'adminlte/login.html')


def index(req):
    print("ovo je log neki")
    log.debug("Ovo je debug")
    # my_task.notify_user(req.user.id, creator=req.user, verbose_name="Moj task")
    my_task.long_task(verbose_name="logn task", creator=req.user)

    log.warning("Sada je {}".format(datetime.datetime.now()))
    #log.warning(f"TZ {timezone.now()}")
    tasks: list[CompletedTask] = CompletedTask.objects.all()
    print(tasks)
    return render(req, "demo/index.html", {"tasks": tasks})


def template(req):
    messages.add_message(req, messages.INFO, 'Ovo je poruka neka...')
    data = {"name": "janko diminic"}
    return render(req, "demo/template.html", data)


def adminlte(req):
    return render(req, "adminlte.html")
