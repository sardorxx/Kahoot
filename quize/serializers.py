from rest_framework import serializers


from quize.models import (Teacher_Subject,
                          Question_Set,
                          Student_Result,
                          Question,
                          Answer)


class TeacherSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher_Subject
        fields = '__all__'



class QuestionSetSerializer(serializers.ModelSerializer):

    class Meta:
       model = Question_Set
       fields = '__all__'



class StudentResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student_Result
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'