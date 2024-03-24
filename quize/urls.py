from django.urls import path

from quize.views import TeacherSubjectList

urlpatterns = [
    path('', TeacherSubjectList.as_view(), name='teacher-subject-list'),
]