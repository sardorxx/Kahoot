from django.contrib.auth import authenticate
from rest_framework import serializers
from account.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['is_active'] = False
        validated_data['user_type'] = "Student"
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LogoutSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        print(data)
        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                pass
            else:
                msg = 'Unable to logout in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg)


class AddTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['user_type'] = 'Teacher'
        validated_data['is_active'] = False
        user = CustomUser.objects.create_user(**validated_data)
        return user


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}


class DeleteTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']
        extra_kwargs = {'password': {'write_only': True}}


class DeleteAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class EmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.IntegerField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
