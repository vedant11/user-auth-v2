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
    # Authorisation
    def get(self, request):
        # Authorized
        token=request.META(['Authorization'])
        decoded_token=json.load(jwt.decode(token, 'secret', algorithms=['HS256']))
        auth_res=decoded_token['resource']
        if auth_res=='Authorized':
            detail_list = list(User.objects.values())
            return JsonResponse(detail_list, safe=False)
        else:
            return JsonResponse({"authorized":"false"})


def specificUserDetails(request, user_id):
    # req_object=json.loads(request.body.decode('utf-8'))
    print(User.objects.get(id=user_id))
    return JsonResponse({"username": User.objects.get(id=user_id).username})


def generateJWT(req_un, req_pass):
    exp_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    JWT_PAYLOAD = {
        "user": {
            "password": req_pass,
            "username": req_un,
        },
        "exp": int(exp_time.timestamp()),
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
        def get_client_ip(request):
            x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
            if x_forwarded_for:
                ip = x_forwarded_for.split(",")[0]
            else:
                ip = request.META.get("REMOTE_ADDR")
            return ip
            # Performing a simple python post request to let the API know someone has authenticated
            # and is served the response successfully
            payload = {"user": user_profile.id, "ip": get_client_ip(request)}
            r = request.post(
                "https://encrusxqoan0b.x.pipedream.net/", data=json.dumps(payload)
            )
        # print(decoded)
        return JsonResponse({"token": token, "success": "true"})
    else:
        return JsonResponse({"success": "false"})


@csrf_exempt
def login(request):
    data = json.loads(request.body.decode('utf-8'))
    token = data['token']
    usr = data['username']
    pas = data['password']
    decoded = jwt.decode(token, 'secret', algorithms='HS256')
    if decoded['user']['password'] == pas and decoded['user']['username'] == usr and int(decoded['exp']) <= int(datetime.datetime.now().timestamp()):
        return JsonResponse({"login-success": "true"})
    else:
        return JsonResponse({"login-success": "false"})


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
