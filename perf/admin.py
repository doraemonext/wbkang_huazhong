# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from django.forms import ModelForm, PasswordInput
from perf.models import Area, Job, Staff


class AreaAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'weight')

    sortable = 'order'


class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'bonus_base', 'job_weight', 'sale_target_percent', 'exam_target_percent', 'profit_target_percent', 'has_trial')

    def sale_target_percent(self, obj):
        return "%d%%" % (obj.sale_target * 100)

    def exam_target_percent(self, obj):
        return "%d%%" % (obj.exam_target * 100)

    def profit_target_percent(self, obj):
        return "%d%%" % (obj.profit_target * 100)

    sale_target_percent.short_description = '销售指标'
    exam_target_percent.short_description = '考核指标'
    profit_target_percent.short_description = '利润达成指标'


class StaffAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name', 'gender', 'department', 'job', 'area', 'entry_date', 'cost_center', 'department_desc', 'cost_center_number', 'status_verbose')

    def status_verbose(self, obj):
        status = obj.get_status()
        if status == Staff.STATUS_ACTIVE:
            return "正式"
        elif status == Staff.STATUS_TRIAL:
            return "试用"
        else:
            return "离职"

    status_verbose.short_description = '状态'

    def suit_row_attributes(self, obj, request):
        css_class = {
            Staff.STATUS_ACTIVE: 'success',
            Staff.STATUS_TRIAL: 'warning',
            Staff.STATUS_INACTIVE: 'error',
        }.get(obj.get_status())
        if css_class:
            return {'class': css_class}


admin.site.register(Area, AreaAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Staff, StaffAdmin)
