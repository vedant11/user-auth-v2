from django.urls import path

from .views import AllUsersDetails, register, specificUserDetails, loginAndGenerateJWT, login

urlpatterns = [
    path('details/', AllUsersDetails.as_view()),
    path('details/<int:user_id>', specificUserDetails),
    path('register/', register),
    path('jwt-auth/', loginAndGenerateJWT),
    path('jwt-auth/login', login)
]
