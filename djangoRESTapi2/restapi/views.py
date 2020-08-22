from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
# Create your views here.

from .models import User


class AllUsersDetails(View):
    def get(self, request):
        detail_list = list(User.objects.values())
        return JsonResponse(detail_list, safe=False)
