# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import LoginServializer
from perf.models import Staff


class LoginAPI(APIView):
    """
    用户登录 API
    """
    serializer_class = LoginServializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        identifier = serializer.validated_data['identifier']
        password = serializer.validated_data['password']

        staff_list = Staff.objects.filter(identifier=identifier)
        if not staff_list.exists():
            return Response({
                'code': 1,
                'message': '员工号不存在',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff = staff_list[0]
        if password != staff.password:
            return Response({
                'code': 2,
                'message': '密码错误',
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'code': 0,
            'message': '',
        }, status=status.HTTP_200_OK)
