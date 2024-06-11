from django.urls import path
from register_app import views

urlpatterns = [
    path("", views.user_lists, name= "home"),
    path("hello/", views.hello, name="hello"),
    path("add/", views.add, name="add"),
]