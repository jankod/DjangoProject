import datetime
from datetime import timezone

import django
from background_task.models import Task, CompletedTask
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, request

from logging import getLogger

from django.shortcuts import render

from django.contrib import messages

from django.shortcuts import HttpResponseRedirect
from django.utils.timezone import now
from django_tables2 import tables, RequestConfig

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


class TaskTable(tables.Table):
    class Meta:
        model = CompletedTask


def tasks(request):
    table = TaskTable(CompletedTask.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=3)
    RequestConfig(request).configure(table)
    return render(request, "demo/tasks.html", {'table': table})


def index(req):
    now = django.utils.timezone.now()

    # pending tasks will have `run_at` column greater than current time.
    # Similar for running tasks, it shall be
    # greater than or equal to `locked_at` column.
    # Running tasks won't work with SQLite DB,
    # because of concurrency issues in SQLite.
    pending_tasks_qs = Task.objects.filter(run_at__gt=now)
    running_tasks_qs = Task.objects.filter(locked_at__gte=now)

    # Completed tasks goes in `CompletedTask` model.
    # I have picked all, you can choose to filter based on what you want.
    completed_tasks_qs = CompletedTask.objects.all()

    print("ovo je log neki")
    log.debug("Ovo je debug")
    # my_task.notify_user(req.user.id, creator=req.user, verbose_name="Moj task")
    my_task.long_task(verbose_name="logn task", creator=req.user)

    log.warning("Sada je {}".format(datetime.datetime.now()))
    # log.warning(f"TZ {timezone.now()}")
    tasks: list[CompletedTask] = CompletedTask.objects.all()
    print(tasks)
    return render(req, "demo/index.html", {"tasks": tasks})


def template(req):
    messages.add_message(req, messages.INFO, 'Ovo je poruka neka...')
    data = {"name": "janko diminic"}
    return render(req, "demo/template.html", data)


def adminlte(req):
    return render(req, "adminlte.html")
