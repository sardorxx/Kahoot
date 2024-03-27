import string
import random

from django.contrib.auth import authenticate, logout
from django.core.cache import cache
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.internal import send_mail
from .models import CustomUser
from .serializers import UserSerializer, LogoutSerializer, AddTeacherSerializer, TeacherListSerializer, \
    DeleteTeacherSerializer, DeleteAccountSerializer, EmailVerificationSerializer, LoginSerializer


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
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = {
                'message': 'You have successfully logged in.'
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomSignupView(APIView):
    permission_classes = ()
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data.get('email')
            confirmation_code = ''.join(random.choices(string.digits, k=6))
            cache.set(email, confirmation_code, timeout=180)
            msg = f'Your confirmation code is {confirmation_code}'
            send_mail(email=email, message_user=msg)

            data = {
                'message': 'You have successfully sign up.'
            }
            serializer.save()
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddTeacherView(APIView):
    permission_classes = ()
    queryset = CustomUser.objects.all()
    serializer_class = AddTeacherSerializer

    def post(self, request):
        serializer = AddTeacherSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data['email']
            confirmation_code = ''.join(random.choices(string.digits, k=6))
            cache.set(email, confirmation_code, timeout=180)
            msg = f'Your confirmation code is {confirmation_code}'
            send_mail(email=email, message_user=msg)
            serializer.save()
            return Response(data={'message': "We are sent code to your email"}, status=status.HTTP_200_OK)
        return Response(data={'message': 'Something wants wrong'}, status=status.HTTP_400_BAD_REQUEST)


class EmailVerificationView(APIView):
    permission_classes = ()
    queryset = CustomUser.objects.all()
    serializer_class = EmailVerificationSerializer

    def post(self, request):
        email = request.POST.get('email')
        s = request.data['email']
        entered_code = request.POST.get('confirmation_code')
        cached_code = cache.get(email)
        if cached_code == entered_code:
            print(email)
            user = CustomUser.objects.get(email=s)
            print(user)
            user.is_active = True
            user.save()
            cache.delete(email)

            return Response(data={'message': 'Your email has been verified'}, status=status.HTTP_200_OK)
        return Response(data={'message': 'Something wants wrong'}, status=status.HTTP_400_BAD_REQUEST)


class DeleteAccountView(APIView):
    permission_classes = ()
    queryset = CustomUser.objects.all()
    serializer_class = DeleteAccountSerializer

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, email=email, password=password)
        if user:
            user.is_active = False
            user.save()
            return Response(data={'messages': 'Your account deleted successfully'}, status=status.HTTP_200_OK)
        return Response(data={'messages': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)


class TeachersListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(user_type="Teacher")
    serializer_class = TeacherListSerializer


class DeleteTeacherView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = DeleteTeacherSerializer

    def post(self, request):
        email = request.data["email"]
        user = CustomUser.objects.get(email=email, user_type="Teacher")
        if user:
            user.is_active = False
            user.save()
            return Response(data={'messages': 'Your account deleted successfully'}, status=status.HTTP_200_OK)
        return Response(data={'messages': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
