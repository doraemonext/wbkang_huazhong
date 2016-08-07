# -*- coding: utf-8 -*-

from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


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
