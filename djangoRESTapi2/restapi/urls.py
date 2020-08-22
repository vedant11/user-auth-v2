from django.urls import path

from .views import AllUsersDetails

urlpatterns = [
    path('', AllUsersDetails.as_view())
]
