from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

from .models import User
import jwt
import datetime


class AllUsersDetails(View):
    def get(self, request):
        detail_list = list(User.objects.values())
        return JsonResponse(detail_list, safe=False)


def specificUserDetails(request, user_id):
    # req_object=json.loads(request.body.decode('utf-8'))
    print(User.objects.get(id=user_id))
    return JsonResponse({"username": User.objects.get(id=user_id).username})


def generateJWT():
    exp_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    JWT_PAYLOAD = {
        "context": {
            "user": {
                "id": "My Name",
                "username": "My Email",
            },
            "iss": "My ISS",
            "exp": int(exp_time.timestamp()),
            "iat": int(datetime.datetime.now().timestamp()),
        }
    }
    jwt_token = jwt.encode(JWT_PAYLOAD, settings.JWT_SECRET, algorithm='HS256')


@csrf_exempt
def loginAndGenerateJWT(request):
    pass


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
