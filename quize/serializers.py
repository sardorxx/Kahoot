import uuid

from django.db.models import Q
from rest_framework import serializers, status

from quize.models import (Teacher_Subject,
                          Question_Set,
                          Student_Result,
                          Question,
                          Answer)
from quize.services import validate_unique_subject


class TeacherSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_Subject
        fields = '__all__'

    def validate(self, data):
        validate_unique_subject(data=data)
        return data


class QuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question_Set
        fields = ['qs_id', 'level', 'user_email', 'subject', 'time_set', 'amount_set']


class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Result
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'is_correct')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'

