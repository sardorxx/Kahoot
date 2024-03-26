from django.urls import path
from account.views import (CustomLoginView, CustomSignupView, CustomLogoutView, AddTeacherView,
                           EmailVerificationView, DeleteAccountView, TeachersListView)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('add_teacher/', AddTeacherView.as_view(), name='add-teacher'),
    path('emailverification/', EmailVerificationView.as_view(), name='email-verification'),
    path('delete_account/', DeleteAccountView.as_view(), name='delete-account'),
    path('get_teachers_list/', TeachersListView.as_view(), name='teachers-list')
]
