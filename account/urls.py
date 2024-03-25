from django.urls import path
from account.views import CustomLoginView, CustomSignupView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]
