from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status, generics, views, permissions
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.db.models import Count
from django.shortcuts import get_object_or_404

from kavenegar import *
from shoe_stores.settings import kave_negar_token_send
from random import randint

from manager.models import User
from manager.serializer import (AdminRegisterationSerializer, LoginAdminSerializer, AdminPanelSerializer,
                                AdminManagerSerializer, SendPhoneSerializer, AdminResetPassword,
                                AdminChangePasswordSerializer, )


class LoginAdminView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = LoginAdminSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username, password=password)
                    
            if user is not None:
                login(request, user)
                return Response({'msg':'login success...'}, status=status.HTTP_200_OK)
        
        return Response({'errors': {'non_field_errors':['username or password is not valid!!']}},
                        status=status.HTTP_404_NOT_FOUND)


class AdminRegisterationView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        serializer = AdminRegisterationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg': 'registeration successfully...'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class AdminProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = User.objects.get(id=request.user.id)
        serializer = AdminPanelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, fromat=None):
        user = User.objects.get(id=request.user.id)
        serializer = AdminPanelSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'your profile was update...'}, status=status.HTTP_200_OK)


class AdminListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = AdminManagerSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AdminDeleteView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]    
    def delete(self, request, format=None):
        user = User.objects.get(id=request.user.id)
        user.delete()
        return Response({'msg': 'deleted....'}, status=status.HTTP_204_NO_CONTENT)


class AdminLogout(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class SendPhone(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = SendPhoneSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            code = randint(1000, 9999)
            user = User.objects.get(phone=serializer.data[phone])
            user.code = code
            user.save()
            kave_negar_token_send(serializer.data['phone'], int(code))
            return Response(user.id, status=status.HTTP_201_CREATED)


class AdminResetPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        serializer = AdminResetPassword(data=request.data, context={'user': user})
        if serializer.is_valid(raise_exception=True):
                reset = User.objects.get(id=pk)
                reset.set_password(request.data.get('password'))
                reset.code = randint(1000, 9999)
                reset.save()
                return Response({'msg': 'your password is reset...'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminChangePassword(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = AdminChangePasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            reset = User.objects.get(username=request.user)
            reset.set_password(request.data.get('password'))
            reset.save()
            return Response({'msg': 'your password is change...'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
