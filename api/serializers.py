# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework import serializers


class LoginServializer(serializers.Serializer):
    identifier = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)
    openid = serializers.CharField(required=True, allow_blank=False)


class Calc1ToNSerializer(serializers.Serializer):
    current_client_reach = serializers.FloatField(required=True)
    current_sfa_reach = serializers.FloatField(required=True)
    others = serializers.CharField(required=True, allow_blank=False)

    def validate(self, data):
        others_list = data['others'].split(',')
        data['others'] = others_list
        return data


class Calc1To1Serializer(serializers.Serializer):
    current_client_reach = serializers.FloatField(required=True)


class CalcNTo1Serializer(serializers.Serializer):
    current_client_reach = serializers.FloatField(required=True)


class BonusHistorySerializer(serializers.Serializer):
    date = serializers.CharField(max_length=10, required=True, allow_blank=False)

    def validate(self, data):
        date = data['date']
        if len(date) != 7:
            raise serializers.ValidationError("不合法的日期")
        date_list = date.split('/')
        if len(date_list) != 2:
            raise serializers.ValidationError("不合法的日期")

        try:
            year = int(date_list[0])
            month = int(date_list[1])
        except ValueError:
            raise serializers.ValidationError("不合法的日期")

        if year < 1900 or year > 2100 or month < 1 or month > 12:
            raise serializers.ValidationError("不合法的日期")

        data['year'] = year
        data['month'] = month
        return data
