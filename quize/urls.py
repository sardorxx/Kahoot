from django.urls import path
from quize.views import (TeacherSubjectList,
                         QuestionSetAPIView,
                         AddQuestionAPIView,
                         QuestionSetListAPIView)
urlpatterns = [
    path('add_subject/', TeacherSubjectList.as_view(), name='teacher-subject-list'),
    path('add_question_set/', QuestionSetAPIView.as_view(), name='add-question-set'),
    path('add_question/', AddQuestionAPIView.as_view(), name='add-question'),
    path('get_question_set/', QuestionSetListAPIView.as_view(), name='question-set-list'),
]