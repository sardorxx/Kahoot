from django.urls import path
from account.views import (CustomLoginView, CustomSignupView, CustomLogoutView, AddTeacherView,
                           EmailVerificationView)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('add_teacher/', AddTeacherView.as_view(), name='add-teacher'),
    path('emailverification/', EmailVerificationView.as_view(), name='email-verification'),
]
