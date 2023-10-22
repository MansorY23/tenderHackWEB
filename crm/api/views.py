from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from api.models import Logs
from api.serializer import LogSerializer, EmailSerializer
from .email_work import send_email_django


class Crud(generics.ListCreateAPIView):
   queryset = Logs.objects.filter(id=id)
   serializer_class = LogSerializer
   permissions_classes = IsAuthenticated


class MessageSenderAPI(APIView):

    def get(self, request):
        subject = self.request.GET.get('subject')
        recipient_list = self.request.GET.get('recipient_list')

        body = self.request.GET.get('message')
        txt_ = self.request.GET.get('text')
        html_ = self.request.GET.get('html')

        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)

        if recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        else:

            send_email_django(subject=subject,
                              user_list=recipient_list,
                              message=body)
            return Response({'msg': 'Okay!'}, status=200)

    def post(self, request):

        subject = self.request.POST.post('subject')
        recipient_list = self.request.POST.post('recipient_list')

        body = self.request.POST.post('message')
        txt_ = self.request.POST.post('te+xt')
        html_ = self.request.POST.post('html')

        if subject is None and txt_ is None and html_ is None and recipient_list is None:
            return Response({'msg': 'There must be a subject, a recipient list, and either HTML or Text.'}, status=200)

        if recipient_list is None:
            return Response({'msg': 'Recipient List required.'}, status=200)
        else:

            send_email_django(subject=subject,
                              user_list=recipient_list,
                              message=body)
            return Response({'msg': 'Okay!'}, status=200)


class EmailAPI(APIView):

    def post(self, request):
        my_data = [{'email': 'arsa2003@mail.ru'}]
        results = EmailSerializer(my_data, many=True).data

