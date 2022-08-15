from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status, generics, views, permissions, mixins
from rest_framework.response import Response

from random import randint
from kavenegar import *
from social_media.settings import kave_negar_token_send

from api_list import api_list

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.db.models import Count
from accounts.models import Accounts, Validation
from accounts.serializer import (PhoneSerializer, CodeSerializer, UserRegisterationSerializer)


class SendPhoneNumber(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            code = randint(1000, 9999)
            valid = serializer.save()
            valid.code = code
            valid.save()
            kave_negar_token_send(serializer.data['phone'], int(code))
            return Response(valid.id, status=status.HTTP_201_CREATED)


class RegisterationView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, pk, format=None):
        valid = Validation.objects.get(id=pk)
        serializer = CodeSerializer(data=request.data, context={'valid': phone})
        if serializer.is_valid(raise_exception=True):
            serializer2 = UserRegisterationSerializer(request.data)
            if serializer2.is_valid(raise_exception=True):
                serializer2.save()
                valid.delete()
                return Response(serializer2.data, status=status.HTTP_200_OK)
        return Response({'msg': 'your code is wrong!!'}, status=status.HTTP_400_BAD_REQUEST)
