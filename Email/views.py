from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .helper import email_registration_detail


class Send_Email(APIView):
    def post(self,request):
        try:
            result = email_registration_detail(request.data,request.FILES)
            return Response(result,status=status.HTTP_200_OK)
        except AttributeError as e:
            return Response({'msg':'{0}'.format(e),'status':'400'},status=status.HTTP_400_BAD_REQUEST)
