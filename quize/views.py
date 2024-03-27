import uuid

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from quize.models import Teacher_Subject, Question_Set, Question, Answer
from quize.serializers import TeacherSubjectSerializer, QuestionSetSerializer, QuestionSerializer


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
        qs = Question_Set.objects.first()
        q_id = uuid.uuid4()
        ques = Question.objects.create(question_id=q_id, text=data['questions'], qs_id=qs)
        for i in data['answers']:
            Answer.objects.create(question_id=ques, text=i['text'], is_correct=i['is_correct'])
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
