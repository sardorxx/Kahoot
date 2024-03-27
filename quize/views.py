from django.shortcuts import get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from quize.models import Teacher_Subject, Question_Set, Question, Answer
from quize.serializers import TeacherSubjectSerializer, QuestionSetSerializer, QuestionSerializer


# Create your views here.
class TeacherSubjectList(APIView):
    queryset = Teacher_Subject.objects.all()
    serializer_class = TeacherSubjectSerializer

    def post(self, request):
        serializer = TeacherSubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionSetAPIView(APIView):
    queryset = Question_Set.objects.all()
    serializer_class = QuestionSetSerializer

    def post(self, request):
        serializer = QuestionSetSerializer(data=request.data, files=None)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddQuestionAPIView(APIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionSetListAPIView(generics.ListAPIView):
    queryset = Question_Set.objects.all()
    serializer_class = QuestionSetSerializer


class QuizViewSet(APIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def post(self, request):
        data = request.data
        print(data)
        return Response(data=data, status=status.HTTP_200_OK)

    # def perform_create(self, serializer):
    #     serializer.save()

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     quiz = serializer.save()
    #     data = data['questions']
    #     question = Question(quiz=quiz, text=data['text'])
    #     question.save()
    #     for answer_data in data['answers']:
    #         Answer.objects.create(question=question, text=answer_data['text'],
    #                               is_correct=answer_data['is_correct', False])
    #
    #     return serializer.data
