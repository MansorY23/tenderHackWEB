from django.urls import path
from django.contrib import admin

from api.views import *

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("api/v1/send", MessageSenderAPI.as_view(), name="email"),

]