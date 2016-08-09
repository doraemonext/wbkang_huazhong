# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers import LoginServializer, BonusHistorySerializer, Calc1ToNSerializer, Calc1To1Serializer, CalcNTo1Serializer, Info1To1Serializer, Info1ToNSerializer, InfoNTo1Serializer
from perf.models import Staff, BonusHistory, ClientTarget, StaffTarget, Staff
from api.utils import convert_sale_to_bonus


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

        if len(staff.openid) == 0:
            staff.openid = openid
            staff.save()
        return Response({
            'code': 0,
            'identifier': identifier,
            'message': '',
        }, status=status.HTTP_200_OK)


class Info1ToNAPI(APIView):
    """
    信息查询 一个客户多个业务 API
    """
    serializer_class = Info1ToNSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        openid = serializer.validated_data['openid']

        staff_list = Staff.objects.filter(openid=openid)
        if not staff_list.exists():
            return Response({
                'code': 1,
                'message': '员工不存在',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff = staff_list[0]

        today = datetime.date.today()
        year = today.year
        month = today.month
        staff_target_list = StaffTarget.objects.filter(staff=staff, client_target__year=year, client_target__month=month)
        if not staff_target_list.exists():
            return Response({
                'code': 2,
                'message': '您本月没有任何目标客户',
            }, status=status.HTTP_400_BAD_REQUEST)
        if len(staff_target_list) > 1:
            return Response({
                'code': 3,
                'message': '您本月有一个以上的目标客户, 非此类别, 请返回重新选择',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff_target = staff_target_list[0]
        client_target = staff_target.client_target

        slist = StaffTarget.objects.filter(client_target=client_target)
        if len(slist) <= 1:
            return Response({
                'code': 4,
                'message': '您本月对应的目标客户为一对一类型, 非此类别, 请返回重新选择',
            }, status=status.HTTP_400_BAD_REQUEST)

        assign_result = []
        for s in slist:
            if s.staff.identifier == staff.identifier:
                continue
            if s.staff.job.name != staff.job.name:
                continue
            assign_result.append({
                'identifier': s.staff.identifier,
                'job_name': s.staff.job.name,
                'name': s.staff.name,
                'target': s.target,
            })
        return Response({
            'code': 0,
            'message': '',
            'data': {
                'date': "%04d 年 %02d 月" % (year, month),
                'name': staff.name,
                'job_name': staff.job.name,
                'target': staff_target.target,
                'client_name': client_target.client.name,
                'client_identifier': client_target.client.identifier,
                'client_target': client_target.target,
                'assign': assign_result,
            },
        }, status=status.HTTP_200_OK)


class Info1To1API(APIView):
    """
    信息查询 一个客户一个业务 API
    """
    serializer_class = Info1To1Serializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        openid = serializer.validated_data['openid']

        staff_list = Staff.objects.filter(openid=openid)
        if not staff_list.exists():
            return Response({
                'code': 1,
                'message': '员工不存在',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff = staff_list[0]

        today = datetime.date.today()
        year = today.year
        month = today.month
        staff_target_list = StaffTarget.objects.filter(staff=staff, client_target__year=year, client_target__month=month)
        if not staff_target_list.exists():
            return Response({
                'code': 2,
                'message': '您本月没有任何目标客户',
            }, status=status.HTTP_400_BAD_REQUEST)
        if len(staff_target_list) > 1:
            return Response({
                'code': 3,
                'message': '您本月有一个以上的目标客户, 非此类别, 请返回重新选择',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff_target = staff_target_list[0]
        client_target = staff_target.client_target

        slist = StaffTarget.objects.filter(client_target=client_target)
        if len(slist) > 1:
            return Response({
                'code': 4,
                'message': '您本月对应的目标客户为一对多类型, 非此类别, 请返回重新选择',
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'code': 0,
            'message': '',
            'data': {
                'date': "%04d 年 %02d 月" % (year, month),
                'name': staff.name,
                'job_name': staff.job.name,
                'target': staff_target.target,
                'client_name': client_target.client.name,
                'client_identifier': client_target.client.identifier,
                'client_target': client_target.target,
            },
        }, status=status.HTTP_200_OK)


class InfoNTo1API(APIView):
    """
    信息查询 多个客户一个业务 API
    """
    serializer_class = InfoNTo1Serializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        openid = serializer.validated_data['openid']

        staff_list = Staff.objects.filter(openid=openid)
        if not staff_list.exists():
            return Response({
                'code': 1,
                'message': '员工不存在',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff = staff_list[0]

        today = datetime.date.today()
        year = today.year
        month = today.month
        staff_target_list = StaffTarget.objects.filter(staff=staff, client_target__year=year, client_target__month=month)
        if not staff_target_list.exists():
            return Response({
                'code': 2,
                'message': '您本月没有任何目标客户',
            }, status=status.HTTP_400_BAD_REQUEST)
        if len(staff_target_list) <= 1:
            return Response({
                'code': 3,
                'message': '您本月没有一个以上的目标客户, 非此类别, 请返回重新选择',
            }, status=status.HTTP_400_BAD_REQUEST)

        client_target_list = []
        total_target = 0
        for staff_target in staff_target_list:
            total_target += staff_target.client_target.target
            client_target_list.append({
                'client_name': staff_target.client_target.client.name,
                'client_identifier': staff_target.client_target.client.identifier,
                'client_target': staff_target.client_target.target,
            })

        return Response({
            'code': 0,
            'message': '',
            'data': {
                'date': "%04d 年 %02d 月" % (year, month),
                'name': staff.name,
                'job_name': staff.job.name,
                'target': total_target,
                'client_target': total_target,
                'client_target_list': client_target_list,
            },
        }, status=status.HTTP_200_OK)


class Calc1ToNAPI(APIView):
    """
    计算 一个客户多个业务 API
    """
    serializer_class = Calc1ToNSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        openid = serializer.validated_data['openid']
        current_client_reach = serializer.validated_data['current_client_reach']
        current_sfa_reach = serializer.validated_data['current_sfa_reach']
        others = serializer.validated_data['others']

        staff_list = Staff.objects.filter(openid=openid)
        if not staff_list.exists():
            return Response({
                'code': 1,
                'message': '员工不存在',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff = staff_list[0]

        today = datetime.date.today()
        year = today.year
        month = today.month
        staff_target_list = StaffTarget.objects.filter(staff=staff, client_target__year=year, client_target__month=month)
        if not staff_target_list.exists():
            return Response({
                'code': 2,
                'message': '您本月没有任何目标客户',
            }, status=status.HTTP_400_BAD_REQUEST)
        if len(staff_target_list) > 1:
            return Response({
                'code': 3,
                'message': '您本月有一个以上的目标客户, 非此类别, 请返回重新选择',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff_target = staff_target_list[0]
        client_target = staff_target.client_target

        slist = StaffTarget.objects.filter(client_target=client_target)
        if len(slist) <= 1:
            return Response({
                'code': 4,
                'message': '您本月对应的目标客户为一对一类型, 非此类别, 请返回重新选择',
            })

        assign_result = []
        for s in slist:
            if s.staff.identifier == staff.identifier:
                continue
            if s.staff.job.name != staff.job.name:
                continue
            assign_result.append({
                'identifier': s.staff.identifier,
                'job_name': s.staff.job.name,
                'name': s.staff.name,
                'target': s.target,
            })

        # Begin to calculate
        # 销售奖金分配总额
        can_assign_amount = (len(assign_result) + 1) * convert_sale_to_bonus(current_client_reach) * staff.job.bonus_base
        if staff.get_status() == Staff.STATUS_TRIAL:
            can_assign_amount *= staff.job.trial_sale_target
        else:
            can_assign_amount *= staff.job.sale_target

        # 奖金系数占比
        total_bonus_ratio = convert_sale_to_bonus(current_sfa_reach)
        for index, assign in enumerate(assign_result):
            total_bonus_ratio += convert_sale_to_bonus(float(others[index]))
        if total_bonus_ratio == 0:
            self_ratio = 0
        else:
            self_ratio = convert_sale_to_bonus(current_sfa_reach) / total_bonus_ratio

        sale_bonus = can_assign_amount * self_ratio * staff.job.job_weight * staff.area.weight
        return Response({
            'code': 0,
            'message': '',
            'data': {
                'sale_bonus': sale_bonus,
            }
        }, status=status.HTTP_200_OK)


class Calc1To1API(APIView):
    """
    计算 一个客户一个业务 API
    """
    serializer_class = Calc1To1Serializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        openid = serializer.validated_data['openid']
        current_client_reach = serializer.validated_data['current_client_reach']

        staff_list = Staff.objects.filter(openid=openid)
        if not staff_list.exists():
            return Response({
                'code': 1,
                'message': '员工不存在',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff = staff_list[0]

        today = datetime.date.today()
        year = today.year
        month = today.month
        staff_target_list = StaffTarget.objects.filter(staff=staff, client_target__year=year, client_target__month=month)
        if not staff_target_list.exists():
            return Response({
                'code': 2,
                'message': '您本月没有任何目标客户',
            }, status=status.HTTP_400_BAD_REQUEST)
        if len(staff_target_list) > 1:
            return Response({
                'code': 3,
                'message': '您本月有一个以上的目标客户, 非此类别, 请返回重新选择',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff_target = staff_target_list[0]
        client_target = staff_target.client_target

        slist = StaffTarget.objects.filter(client_target=client_target)
        if len(slist) > 1:
            return Response({
                'code': 4,
                'message': '您本月对应的目标客户为一对多类型, 非此类别, 请返回重新选择',
            })

        # Begin to calculate
        # 销售奖金分配总额
        can_assign_amount = convert_sale_to_bonus(current_client_reach) * staff.job.bonus_base
        if staff.get_status() == Staff.STATUS_TRIAL:
            can_assign_amount *= staff.job.trial_sale_target
        else:
            can_assign_amount *= staff.job.sale_target

        sale_bonus = can_assign_amount * staff.job.job_weight * staff.area.weight
        return Response({
            'code': 0,
            'message': '',
            'data': {
                'sale_bonus': sale_bonus,
            }
        }, status=status.HTTP_200_OK)


class CalcNTo1API(APIView):
    """
    计算 多个客户一个业务 API
    """
    serializer_class = CalcNTo1Serializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        openid = serializer.validated_data['openid']
        current_client_reach = serializer.validated_data['current_client_reach']

        staff_list = Staff.objects.filter(openid=openid)
        if not staff_list.exists():
            return Response({
                'code': 1,
                'message': '员工不存在',
            }, status=status.HTTP_400_BAD_REQUEST)
        staff = staff_list[0]

        today = datetime.date.today()
        year = today.year
        month = today.month
        staff_target_list = StaffTarget.objects.filter(staff=staff, client_target__year=year, client_target__month=month)
        if not staff_target_list.exists():
            return Response({
                'code': 2,
                'message': '您本月没有任何目标客户',
            }, status=status.HTTP_400_BAD_REQUEST)
        if len(staff_target_list) <= 1:
            return Response({
                'code': 3,
                'message': '您本月没有一个以上的目标客户, 非此类别, 请返回重新选择',
            }, status=status.HTTP_400_BAD_REQUEST)

        client_target_list = []
        total_target = 0
        for staff_target in staff_target_list:
            total_target += staff_target.client_target.target
            client_target_list.append({
                'client_name': staff_target.client_target.client.name,
                'client_identifier': staff_target.client_target.client.identifier,
                'client_target': staff_target.client_target.target,
            })

        # Begin to calculate
        # 销售奖金分配总额
        can_assign_amount = convert_sale_to_bonus(current_client_reach) * staff.job.bonus_base
        if staff.get_status() == Staff.STATUS_TRIAL:
            can_assign_amount *= staff.job.trial_sale_target
        else:
            can_assign_amount *= staff.job.sale_target

        sale_bonus = can_assign_amount * staff.job.job_weight * staff.area.weight
        return Response({
            'code': 0,
            'message': '',
            'data': {
                'sale_bonus': sale_bonus,
            }
        }, status=status.HTTP_200_OK)


class BonusHistoryAPI(APIView):
    """
    奖金历史记录 API
    """
    serializer_class = BonusHistorySerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        openid = serializer.validated_data['openid']
        year = serializer.validated_data['year']
        month = serializer.validated_data['month']

        history_list = BonusHistory.objects.filter(year=year, month=month, staff__openid=openid)
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
