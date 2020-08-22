from django.urls import path

from .views import AllUsersDetails, register

urlpatterns = [
    path('details/', AllUsersDetails.as_view()),
    path('register/', register)
]
