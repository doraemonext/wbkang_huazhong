# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import LoginServializer, BonusHistorySerializer
from perf.models import Staff, BonusHistory


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
                'message': '该员工已绑定过其他微信账户, 请联系管理员删除绑定'
            }, status=status.HTTP_400_BAD_REQUEST)

        request.session['identifier'] = identifier
        if len(staff.openid) == 0:
            staff.openid = openid
            staff.save()
        return Response({
            'code': 0,
            'identifier': identifier,
            'message': '',
        }, status=status.HTTP_200_OK)


class BonusHistoryAPI(APIView):
    """
    奖金历史记录 API
    """
    serializer_class = BonusHistorySerializer

    def get(self, request, *args, **kwargs):
        identifier = request.session.get('identifier')
        if not identifier:
            return Response({
                'code': -1,
                'message': '尚未登录'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        year = serializer.validated_data['year']
        month = serializer.validated_data['month']

        history_list = BonusHistory.objects.filter(year=year, month=month, staff__identifier=identifier)
        if not history_list.exists():
            return Response({
                'code': 1,
                'message': '尚无您 %d 年 %d 月的绩效奖金记录' % (year, month),
            }, status=status.HTTP_400_BAD_REQUEST)

        history = history_list[0]
        return Response({
            'code': 0,
            'message': '',
            'data': {
                'name': history.name,
                'job_name': history.job_name,
                'bonus_base': history.bonus_base,
                'job_weight': history.job_weight,
                'area_weight': history.area_weight,
                'last_month_reach': history.last_month_reach,
                'current_month_reach': history.current_month_reach,
                'sfa_reach': history.sfa_reach,
                'sale_bonus': history.sale_bonus,
                'exam_bonus': history.exam_bonus,
                'total_bonus': history.sale_bonus + history.exam_bonus,
            }
        }, status=status.HTTP_200_OK)


class BonusHistoryDateListAPI(APIView):
    """
    奖金历史记录日期列表 API
    """
    def get(self, request, *args, **kwargs):
        month_date = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
        res = []
        for i in range(0, 24):
            res.append({
                'value': '%04d/%02d' % (month_date.year, month_date.month),
                'text': '%04d 年 %02d 月' % (month_date.year, month_date.month),
            })
            month_date = month_date.replace(day=1) - datetime.timedelta(days=1)
        return Response({
            'code': 0,
            'message': '',
            'data': res,
        }, status=status.HTTP_200_OK)
