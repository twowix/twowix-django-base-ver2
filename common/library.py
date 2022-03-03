import datetime
import json
from datetime import datetime
from datetime import timedelta

import requests
from common.response_code import *
from django.conf import settings
from rest_framework.exceptions import APIException
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response

JSON_CODE = "code"
JSON_MESSAGE = "message"
JSON_DATA = "data"
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


######################################################
# Common
######################################################
# API 응답
def APIResponse(code, data=None):
    response_data = {
        'code': code,
        'message': code_to_message(code),
        'data': data
    }
    return Response(response_data)


######################################################
# HTTP req/res 관련
######################################################
def response_serializer(code, data=None):
    json_data = dict()
    json_data[JSON_CODE] = code
    json_data[JSON_MESSAGE] = code_to_message(code)
    json_data[JSON_DATA] = data
    return json_data


def mandatory_key(request, name):
    try:
        if request.method == 'GET':
            data = request.GET[name]
        else:
            data = request.POST[name]
        if data == '':
            raise APIException(STATUS_MISSING_MANDATORY_PARAM)
    except:
        try:
            json_body = request.data
            data = json_body[name]
            if data == "":
                raise APIException(STATUS_MISSING_MANDATORY_PARAM)
        except:
            raise APIException(STATUS_MISSING_MANDATORY_PARAM)
    return data


def optional_key(request, name, default_value=''):
    try:
        if request.method == 'GET':
            data = request.GET[name]
        else:
            data = request.POST[name]
        if data in ["", None, 'null', 'undefined']:
            data = default_value
    except:
        try:
            json_body = request.data
            data = json_body[name]
            if data in ["", None, 'null', 'undefined']:
                data = default_value
        except:
            data = default_value
    return data


######################################################
# 날짜 관련
######################################################
def get_now(): return datetime.now()


def get_after_day(d): return get_now() + timedelta(days=d)


def get_before_min(m): return get_now() + timedelta(seconds=(-60 * m))


def get_before_day(d): return get_now() + timedelta(days=(-d))


def get_after_min(m): return get_now() + timedelta(seconds=(60 * m))


######################################################
# 페이징 & API 용
######################################################
def paging(request):
    try:
        page = int(request.GET.get('page', 1)) - 1
        size = int(request.GET.get('size', 10))
        if request.path.split('/')[1] != "cms-api" and size > 30:
            raise APIException(STATUS_MAX_SIZE_OVER)
        start_row = page * size
        end_row = (page + 1) * size
    except APIException as e:
        raise APIException(e)
    return start_row, end_row


######################################################
# soical oauth 검증
######################################################
def facebook_validator(access_token):
    data = requests.get(
        'https://graph.facebook.com/me',
        {'access_token': access_token}
    )
    if data.status_code != 200:
        return False
    else:
        data = json.loads(data.text)
        return_data = {
            "id": data["id"],
            "gender": None,
            "phone": None,
            "birth": None,
            "email": None,
            "name": None,
        }
        return return_data


def kakao_validator(access_token):
    access_data = requests.post(
        'https://kauth.kakao.com/oauth/token',
        data={
            "grant_type": "authorization_code",
            "client_id": settings.KAKAO_API_KEY,
            "redirect_uri": settings.KAKAO_REDIRECT_URL,
            "client_secret": settings.KAKAO_SECRET_KEY,
            "code": access_token
        }
    )
    if access_data.status_code != 200:
        return False

    user_access_code = json.loads(access_data.text)["access_token"]
    headers = {
        "Authorization": "Bearer " + user_access_code
    }
    data = requests.get(
        'https://kapi.kakao.com/v2/user/me',
        headers=headers
    )
    if data.status_code != 200:
        return False
    else:
        data = json.loads(data.text)
        birth = None
        if "kakao_account" in data.keys():
            try:
                birth = data["kakao_account"]["birthyear"] + data["kakao_account"]["birthday"]
                birth = datetime.strptime(birth, '%Y%m%d')

                return_data = {
                    "id": data["id"],
                    "gender": data["kakao_account"]["gender"] if data["kakao_account"]["gender"] else None,
                    "phone": data["kakao_account"]["phone_number"].replace("+82 ", "0").replace("-", "").replace(
                        " ", ""
                        ) if data["kakao_account"]["phone_number"] else None,
                    "birth": birth,
                    "email": data["kakao_account"]["email"] if data["kakao_account"]["email"] else None,
                    "name": data["kakao_account"]["profile"]["nickname"] if data["kakao_account"]["profile"][
                        "nickname"] else None,
                }
            except:
                return_data = {
                    "id": data["id"],
                    "gender": None,
                    "phone": None,
                    "birth": birth,
                    "email": None,
                    "name": None,
                }
        else:
            return_data = {
                "id": data["id"],
                "gender": None,
                "phone": None,
                "birth": birth,
                "email": None,
                "name": None,
            }
        return return_data
