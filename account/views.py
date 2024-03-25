from django.contrib.auth import authenticate, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, LogoutSerializer


class CustomLogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, email=email, password=password)
        if user:
            logout(request)
            message = 'You have successfully logged out.'
            return Response(status=status.HTTP_201_CREATED, data={'message': message})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Please enter correct email and password'})


class CustomLoginView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        print(request.data)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'message': 'You have successfully logged in.'
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomSignupView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            email = request.data.get('email')
            token = Token.objects.get_or_create(user=user)
            data = {
                'email': email,
                'token': str(token[0]),
                'message': 'You have successfully registered.'
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
