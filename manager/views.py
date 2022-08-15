from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status, generics, views, permissions
from rest_framework.response import Response

from django.contrib.auth import authenticate
from django.db.models import Count
from django.shortcuts import get_object_or_404

from manager.models import User
from manager.serializer import (AdminRegisterationSerializer, )


class AdminRegisterationView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAdminUser]
    def post(self, request, format=None):
        serializer = AdminRegisterationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg': 'registeration successfully...'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


