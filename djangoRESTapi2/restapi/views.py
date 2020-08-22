# from django.shortcuts import render
# from django.views import View
# from django.http import JsonResponse, HttpResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# # Create your views here.

# from .models import User


# class AllUsersDetails(View):
#     def get(self, request):
#         detail_list = list(User.objects.values())
#         return JsonResponse(detail_list, safe=False)


# class RegisterNewUser(View):

#     def post(self, request):
#         data = request.body.decode('utf8')
#         data = json.loads(data)
#         print(data)
#         try:
#             new_user = User(
#                 username=data["username"], password=data["password"])
#             new_user.save()
#             return JsonResponse({"created": data}, safe=False)
#         except:
#             return JsonResponse({"error": "not a valid data"}, safe=False)


# """

# """

from rest_framework import viewsets

from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
