from django.urls import path
from django.contrib import admin

from api.views import *

urlpatterns = [
    path("api/v1/admin"),
    path("api/v1/all", Crud.as_view() , name="index"),

]