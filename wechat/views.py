# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http.response import HttpResponse
from wechatpy.enterprise.crypto import WeChatCrypto
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.enterprise.crypto import WeChatCrypto
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.enterprise.exceptions import InvalidCorpIdException
from wechatpy.enterprise import parse_message, create_reply
from wechatpy.messages import TextMessage
from wechatpy.events import ClickEvent
from perf.models import Staff


class ProcessorView(View):
    """
    控制中心 View
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProcessorView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        signature = request.GET.get('msg_signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')

        crypto = WeChatCrypto(settings.WECHAT_TOKEN, settings.WECHAT_ENCODING_AES_KEY, settings.WECHAT_CORP_ID)
        try:
            resp = crypto.check_signature(signature, timestamp, nonce, echostr)
        except InvalidSignatureException:
            return HttpResponse("ERROR CHECK SIGNATURE")
        return HttpResponse(resp)

    def post(self, request, *args, **kwargs):
        signature = request.GET.get('msg_signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        crypto = WeChatCrypto(settings.WECHAT_TOKEN, settings.WECHAT_ENCODING_AES_KEY, settings.WECHAT_CORP_ID)
        try:
            decrypted_xml = crypto.decrypt_message(request.body, signature, timestamp, nonce)
        except (InvalidSignatureException, InvalidCorpIdException):
            return HttpResponse("ERROR CHECK SIGNATURE")
        else:
            message = parse_message(decrypted_xml)
            if isinstance(message, TextMessage):
                if message.content == "绩效":
                    xml = create_reply("<a href='%s'>点击此处计算绩效</a>%s" % (settings.BASE_URL + reverse("wechat:login") + "?openid=" + message.source, message.__dict__), message).render()
                    encrypted_xml = crypto.encrypt_message(xml, nonce, timestamp)
                    return HttpResponse(encrypted_xml)
            elif isinstance(message, ClickEvent):
                if message.key == "绩效":
                    xml = create_reply("<a href='%s'>点击此处计算绩效</a>" % (settings.BASE_URL + reverse("wechat:login") + "?openid=" + message.source), message).render()
                    encrypted_xml = crypto.encrypt_message(xml, nonce, timestamp)
                    return HttpResponse(encrypted_xml)
            return HttpResponse("success")


class LoginView(View):
    """
    登录 View
    """
    def get(self, request, *args, **kwargs):
        openid = request.GET.get('openid', '')
        staff = Staff.objects.filter(openid=openid)
        if staff.exists():
            return redirect(reverse('wechat:main_selector') + '?openid=' + openid)

        return render(request, 'wechat/login.html', {'openid': openid})


class MainSelectorView(View):
    """
    主选择器 View
    """
    def get(self, request, *args, **kwargs):
        openid = request.GET.get('openid', '')
        staff = Staff.objects.filter(openid=openid)
        if not staff.exists():
            return redirect(reverse('wechat:login') + '?openid=' + openid)

        return render(request, 'wechat/main_selector.html', {'openid': openid})


class CalcSelectorView(View):
    """
    奖励测算选择器 View
    """
    def get(self, request, *args, **kwargs):
        openid = request.GET.get('openid', '')
        staff = Staff.objects.filter(openid=openid)
        if not staff.exists():
            return redirect(reverse('wechat:login') + '?openid=' + openid)

        return render(request, 'wechat/calc_selector.html', {'openid': openid})


class Calc1ToNView(View):
    """
    一个R3客户对应多个业务 View
    """
    def get(self, request, *args, **kwargs):
        openid = request.GET.get('openid', '')
        staff = Staff.objects.filter(openid=openid)
        if not staff.exists():
            return redirect(reverse('wechat:login') + '?openid=' + openid)

        return render(request, 'wechat/calc_1ton.html', {'openid': openid})


class Calc1To1View(View):
    """
    一个R3客户对应一个业务 View
    """
    def get(self, request, *args, **kwargs):
        openid = request.GET.get('openid', '')
        staff = Staff.objects.filter(openid=openid)
        if not staff.exists():
            return redirect(reverse('wechat:login') + '?openid=' + openid)

        return render(request, 'wechat/calc_1to1.html', {'openid': openid})


class CalcNTo1View(View):
    """
    N个R3客户对应一个业务 View
    """
    def get(self, request, *args, **kwargs):
        openid = request.GET.get('openid', '')
        staff = Staff.objects.filter(openid=openid)
        if not staff.exists():
            return redirect(reverse('wechat:login') + '?openid=' + openid)

        return render(request, 'wechat/calc_nto1.html', {'openid': openid})


class HistoryView(View):
    """
    奖励明细 View
    """
    def get(self, request, *args, **kwargs):
        openid = request.GET.get('openid', '')
        staff = Staff.objects.filter(openid=openid)
        if not staff.exists():
            return redirect(reverse('wechat:login') + '?openid=' + openid)

        return render(request, 'wechat/history.html', {'openid': openid})
