from django.urls import path
from quize.views import (TeacherSubjectList,
                         QuestionSetAPIView,
                         AddQuestionAPIView)

urlpatterns = [
    path('add_subject/', TeacherSubjectList.as_view(), name='teacher-subject-list'),
    path('add_question_set/', QuestionSetAPIView.as_view(), name='add-question-set'),
    path('add_question/', AddQuestionAPIView.as_view(), name='add-question'),
]