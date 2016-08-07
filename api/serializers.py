# -*- coding: utf-8 -*-

from rest_framework import serializers


class LoginServializer(serializers.Serializer):
    identifier = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)
    openid = serializers.CharField(required=True, allow_blank=False)
