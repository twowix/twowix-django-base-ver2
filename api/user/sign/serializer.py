from rest_framework import serializers


class _SubSerializer(serializers.ModelSerializer):
    pass


class MainSerializer(serializers.ModelSerializer):
    sub = _SubSerializer()