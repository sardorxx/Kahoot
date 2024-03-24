from django.db.models import Q
from rest_framework import validators, serializers

from quize.models import Teacher_Subject
from quize.serializers import TeacherSubjectSerializer


# def validate_teacher_subject(data):
#     queryset = Teacher_Subject.objects.get(Q(user_type=data['user_type']) & Q(user_email=data['user_email'])).all()
#     for teacher in queryset:
#         if teacher.subject == data['subject']:
#             raise serializers.ValidationError('Subject Already Exists')
#     return data


