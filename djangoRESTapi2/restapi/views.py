from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

from .models import User


class AllUsersDetails(View):
    def get(self, request):
        detail_list = list(User.objects.values())
        return JsonResponse(detail_list, safe=False)


@csrf_exempt
def register(request):
    req_object = (json.loads(request.body.decode('utf-8')))
    try:
        new_user = User(
            username=req_object['username'], password=req_object['password'])
        new_user.save()
    except:
        return JsonResponse({"success": "not ok"})
    return JsonResponse({"success": "ok"})
