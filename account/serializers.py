from django.contrib.auth import authenticate
from rest_framework import serializers
from account.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'user_type', 'full_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LogoutSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

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
