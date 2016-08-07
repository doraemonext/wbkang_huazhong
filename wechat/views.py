# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http.response import HttpResponse
from wechat_sdk import WechatBasic, WechatConf
from wechat_sdk.messages import TextMessage, EventMessage


class ProcessorView(View):
    """
    控制中心 View
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProcessorView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')

        conf = WechatConf(appid=settings.WECHAT_APPID, appsecret=settings.WECHAT_APPSECRET, token=settings.WECHAT_TOKEN, encrypt_mode='normal')
        basic = WechatBasic(conf=conf)
        if basic.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponse(echostr)
        else:
            return HttpResponse("ERROR CHECK SIGNATURE")

    def post(self, request, *args, **kwargs):
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        conf = WechatConf(appid=settings.WECHAT_APPID, appsecret=settings.WECHAT_APPSECRET, token=settings.WECHAT_TOKEN, encrypt_mode='normal')
        basic = WechatBasic(conf=conf)
        if not basic.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponse("ERROR CHECK SIGNATURE")

        basic.parse_data(request.body)
        message = basic.get_message()
        if isinstance(message, TextMessage):
            if message.content == "绩效":
                return HttpResponse(basic.response_text("<a href='%s'>点击此处计算绩效</a>" % (
                settings.BASE_URL + reverse("wechat:login") + "?openid=" + message.source)))
        elif isinstance(message, EventMessage):
            if message.key == "绩效":
                return HttpResponse(basic.response_text("<a href='%s'>点击此处计算绩效</a>" % (
                settings.BASE_URL + reverse("wechat:login") + "?openid=" + message.source)))
        return HttpResponse(basic.response_none())


class LoginView(View):
    """
    登录 View
    """
    def get(self, request, *args, **kwargs):
        if request.session.get('identifier'):
            return redirect(reverse('wechat:main_selector') + '?openid=' + request.GET.get('openid', ''))
        return render(request, 'wechat/login.html', {
            'openid': request.GET.get('openid', '')
        })


class MainSelectorView(View):
    """
    主选择器 View
    """
    def get(self, request, *args, **kwargs):
        if not request.session.get('identifier'):
            return redirect(reverse('wechat:login') + '?openid=' + request.GET.get('openid', ''))
        return render(request, 'wechat/main_selector.html', {
            'openid': request.GET.get('openid', '')
        })


class CalcSelectorView(View):
    """
    奖励测算选择器 View
    """
    def get(self, request, *args, **kwargs):
        if not request.session.get('identifier'):
            return redirect(reverse('wechat:login') + '?openid=' + request.GET.get('openid', ''))
        return render(request, 'wechat/calc_selector.html', {
            'openid': request.GET.get('openid', '')
        })


class Calc1ToNView(View):
    """
    一个R3客户对应多个业务 View
    """
    def get(self, request, *args, **kwargs):
        if not request.session.get('identifier'):
            return redirect(reverse('wechat:login') + '?openid=' + request.GET.get('openid', ''))
        return render(request, 'wechat/calc_1ton.html', {
            'openid': request.GET.get('openid', '')
        })


class Calc1To1View(View):
    """
    一个R3客户对应一个业务 View
    """
    def get(self, request, *args, **kwargs):
        if not request.session.get('identifier'):
            return redirect(reverse('wechat:login') + '?openid=' + request.GET.get('openid', ''))
        return render(request, 'wechat/calc_1to1.html', {
            'openid': request.GET.get('openid', '')
        })


class CalcNTo1View(View):
    """
    N个R3客户对应一个业务 View
    """
    def get(self, request, *args, **kwargs):
        if not request.session.get('identifier'):
            return redirect(reverse('wechat:login') + '?openid=' + request.GET.get('openid', ''))
        return render(request, 'wechat/calc_nto1.html', {
            'openid': request.GET.get('openid', '')
        })


class HistoryView(View):
    """
    奖励明细 View
    """
    def get(self, request, *args, **kwargs):
        if not request.session.get('identifier'):
            return redirect(reverse('wechat:login') + '?openid=' + request.GET.get('openid', ''))
        return render(request, 'wechat/history.html', {
            'openid': request.GET.get('openid', '')
        })
