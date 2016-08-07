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
        openid = serializer.validated_data['openid']

        if request.session.get('identifier') == identifier:
            return Response({
                'code': 0,
                'identifier': identifier,
                'message': '',
            }, status=status.HTTP_200_OK)

        staff_list = Staff.objects.filter(identifier=identifier)
        if not staff_list.exists():
            return Response({
                'code': 1,
                'identifier': identifier,
                'message': '员工号不存在',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff = staff_list[0]
        if password != staff.password:
            return Response({
                'code': 2,
                'identifier': identifier,
                'message': '密码错误',
            }, status=status.HTTP_400_BAD_REQUEST)
        if len(staff.openid) > 0 and openid != staff.openid:
            return Response({
                'code': 3,
                'identifier': identifier,
                'message': '该员工已绑定过其他微信账户, 请联系管理员'
            })

        if len(staff.openid) == 0:
            staff.openid = openid
            staff.save()
        return Response({
            'code': 0,
            'identifier': identifier,
            'message': '',
        }, status=status.HTTP_200_OK)
