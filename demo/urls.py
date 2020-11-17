from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('t', views.template, name='template'),

    #    path('logout/', views.logout, name='logout'),
    path('adminlte', views.adminlte, name='adminlte'),
    #    path(r'^login', views.login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('login', views.login_user, name='login'),
    path('tasks/', views.tasks, name='tasks')
]
