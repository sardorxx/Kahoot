
from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from quize.models import Teacher_Subject
from quize.serializers import TeacherSubjectSerializer


# Create your views here.
class TeacherSubjectList(generics.CreateAPIView):
    queryset = Teacher_Subject.objects.all()
    serializer_class = TeacherSubjectSerializer

    def post(self, request):
        serializer = TeacherSubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate(self, data):
        queryset = TeacherSubjectSerializer.objects.get(
            Q(user_type=data['user_type']) & Q(user_email=data['user_email']))
        for teacher in queryset:
            if teacher.subject == data['subject']:
                raise serializers.ValidationError('Subject Already Exists')
        return queryset
# asa