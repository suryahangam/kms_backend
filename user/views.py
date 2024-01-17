from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets

from user.serializers import CustomUserSerializer
from user.models import (CustomUser, Profile)


from user.serializers import (
    EmployeeRegisterSerializer,
    ProfileSerializer
    )


class clientRegistration(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class EmployeeRegistration(generics.CreateAPIView):
    # permission_classes = (AllowAny,)
    queryset = CustomUser.objects.all()
    serializer_class = EmployeeRegisterSerializer


class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(
            username=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)

            return JsonResponse(
                {
                'message': 'Successful',
                'status': 1,
                'data': [{
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                    }
                ]}
            )
        return JsonResponse(
            {
                'message': 'Invalid Credentials',
                'status': 0,
                'data': []
            })


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer