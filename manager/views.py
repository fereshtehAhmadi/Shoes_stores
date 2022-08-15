from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status, generics, views, permissions
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.db.models import Count
from django.shortcuts import get_object_or_404

from manager.models import User
from manager.serializer import (AdminRegisterationSerializer, LoginAdminSerializer, AdminPanelSerializer,
                                AdminManagerSerializer, )

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


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
    permission_classes = [IsStaffUser]
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
