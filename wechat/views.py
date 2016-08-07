# -*- coding: utf-8 -*-

from django.views.generic import View
from django.shortcuts import render


class LoginView(View):
    """
    登录 View
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'wechat/login.html')
    