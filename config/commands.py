import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def create_db(model_name):
    dir = f'db/{model_name}'
    path = os.path.join(BASE_DIR, dir)
    os.mkdir(path)
    f = open(f'{path}/__init__.py', 'w')
    f.close()
    f = open(f'{path}/models.py', 'w')
    f.write('from django.db import models')
    f.close()
    dir = f'db/{model_name}/migrations'
    path = os.path.join(BASE_DIR, dir)
    os.mkdir(path)
    f = open(f'{path}/__init__.py', 'w')
    f.close()


def create_api(api_name, api_list=[]):
    dir = f'api/{api_name}'
    path = os.path.join(BASE_DIR, dir)
    if not os.path.isdir(path):
        os.mkdir(path)
        f = open(f'{path}/_urls.py', 'w')
        f.write(
            'from django.urls import path\n\n'
            'urlpatterns = []'
        )
        f.close()

    if len(api_list):
        for api in api_list:
            dir = f'api/{api_name}/{api}'
            path = os.path.join(BASE_DIR, dir)
            if not os.path.isdir(path):
                os.mkdir(path)
                f = open(f'{path}/view.py', 'w')
                f.write('from rest_framework.views import APIView\nfrom common.library import *')
                f.close()
                f = open(f'{path}/serializer.py', 'w')
                f.write(
                    'from rest_framework import serializers'
                    '\n\n\n'
                    'class _SubSerializer(serializers.ModelSerializer):\n'
                    '\tpass'
                    '\n\n\n'
                    'class MainSerializer(serializers.ModelSerializer):\n'
                    '\tsub = _SubSerializer()'
                )
                f.close()
