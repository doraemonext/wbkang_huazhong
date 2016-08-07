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