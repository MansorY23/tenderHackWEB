from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from models import Logs
from serializer import LogSerializer


class Crud(generics.ListCreateAPIView):
    queryset = Logs.objects.filter(id=id)
    serializer_class = LogSerializer
    permissions_classes = IsAuthenticated


class MessageBroker(generics.CreateAPIView):
    queryset = Logs.objects.filter(id=id)
    serializer_class = LogSerializer
    permission_classes = [IsAdminUser,
                          ]