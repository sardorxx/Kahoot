from rest_framework import generics, status
from rest_framework.response import Response

from quize.models import Teacher_Subject, Question_Set, Question
from quize.serializers import TeacherSubjectSerializer, QuestionSetSerializer, QuestionSerializer


# Create your views here.
class TeacherSubjectList(generics.CreateAPIView):
    queryset = Teacher_Subject.objects.all()
    serializer_class = TeacherSubjectSerializer

    def add_subject(self, request):
        serializer = TeacherSubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionSetAPIView(generics.CreateAPIView):
    queryset = Question_Set.objects.all()
    serializer_class = QuestionSetSerializer

    def add_question_set(self, request):
        serializer = QuestionSetSerializer(data=request.data, files=None)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddQuestionAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def add_question(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddAnswerAPIView(generics.CreateAPIView):
    queryset = Answer.objects.filter()
