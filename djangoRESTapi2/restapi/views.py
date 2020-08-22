from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
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


def generateJWT(req_un, req_pass):
    exp_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    JWT_PAYLOAD = {
        "context": {
            "user": {
                "password": req_pass,
                "username": req_un,
            },
            "iss": "My ISS",
            "exp": int(exp_time.timestamp()),
            "iat": int(datetime.datetime.now().timestamp()),
        }
    }
    jwt_token = jwt.encode(JWT_PAYLOAD, 'secret', algorithm='HS256')
    return jwt_token


@csrf_exempt
def loginAndGenerateJWT(request):
    req_un = json.loads(request.body.decode('utf-8'))['username']
    req_pass = json.loads(request.body.decode('utf-8'))['password']
    act_pass = User.objects.get(username=req_un).password
    token = generateJWT(req_un, req_pass).decode('utf-8')
    # print(type(token.decode('utf-8')))
    if act_pass == req_pass:
        return JsonResponse({"token": token, "success": "true"})
    else:
        return JsonResponse({"success": "false"})


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
