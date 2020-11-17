from time import sleep

from background_task import background
from django.contrib.auth.models import User


@background(schedule=2)
def notify_user(user_id):
    # lookup user by id and send them a message
    user = User.objects.get(pk=user_id)
    print("Ovo je backgroudn task ", user)


@background(schedule=1)
def long_task():
    sleep(6)
    print("long task fisnih")
