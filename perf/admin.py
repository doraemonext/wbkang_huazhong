# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from perf.models import Area, Job, JobMatch, Staff, Client, ClientTarget, StaffTarget, BonusHistory, DataImport


class AreaAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'weight')


class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'bonus_base', 'job_weight', 'sale_target_percent', 'exam_target_percent', 'profit_target_percent', 'has_trial', 'trial_sale_target_percent', 'trial_exam_target_percent')

    def sale_target_percent(self, obj):
        return "%d%%" % (obj.sale_target * 100)

    def exam_target_percent(self, obj):
        return "%d%%" % (obj.exam_target * 100)

    def profit_target_percent(self, obj):
        return "%d%%" % (obj.profit_target * 100)

    def trial_sale_target_percent(self, obj):
        return "%d%%" % (obj.trial_sale_target * 100)

    def trial_exam_target_percent(self, obj):
        return "%d%%" % (obj.trial_exam_target * 100)

    sale_target_percent.short_description = '销售指标'
    exam_target_percent.short_description = '考核指标'
    profit_target_percent.short_description = '利润达成指标'
    trial_sale_target_percent.short_description = '试用期销售指标'
    trial_exam_target_percent.short_description = '试用期考核指标'


class JobMatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name', 'gender', 'department', 'job', 'job_name', 'area', 'entry_date', 'cost_center', 'department_desc', 'cost_center_number', 'status_verbose', 'has_bound')

    def status_verbose(self, obj):
        status = obj.get_status()
        if status == Staff.STATUS_ACTIVE:
            return "正式"
        elif status == Staff.STATUS_TRIAL:
            return "试用"
        else:
            return "离职"

    def has_bound(self, obj):
        if len(obj.openid) > 0:
            return "是"
        else:
            return "否"

    has_bound.short_description = '绑定'
    status_verbose.short_description = '状态'

    def suit_row_attributes(self, obj, request):
        css_class = {
            Staff.STATUS_ACTIVE: 'success',
            Staff.STATUS_TRIAL: 'warning',
            Staff.STATUS_INACTIVE: 'error',
        }.get(obj.get_status())
        if css_class:
            return {'class': css_class}


class ClientAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name')


class StaffTargetInline(admin.StackedInline):
    model = StaffTarget
    min_num = 0
    max_num = 100
    verbose_name = '员工目标'
    verbose_name_plural = '员工目标'


class ClientTargetAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'target')
    inlines = [StaffTargetInline, ]

    def date(self, obj):
        return "%d年%d月" % (obj.year, obj.month)

    date.short_description = '日期'


class StaffTargetAdmin(admin.ModelAdmin):
    list_display = ('staff', 'client_name', 'date', 'client_target_amount',  'target')

    def client_name(self, obj):
        return "%s" % obj.client_target.client.name + ' (' + obj.client_target.client.identifier + ')'

    def client_target_amount(self, obj):
        return "%d" % obj.client_target.target

    def date(self, obj):
        return "%d年%d月" % (obj.client_target.year, obj.client_target.month)

    client_name.short_description = '客户'
    client_target_amount.short_description = '客户目标(元)'
    date.short_description = '日期'


class BonusHistoryAdmin(admin.ModelAdmin):
    exclude = ('name', 'job_name', 'bonus_base', 'job_weight', 'area_weight')
    list_display = ('date', 'staff_name', 'job_name', 'bonus_base', 'job_weight', 'area_weight', 'last_month_reach_percent', 'current_month_reach_percent', 'sfa_reach_percent', 'sale_bonus', 'exam_bonus', 'total_bonus')

    def date(self, obj):
        return "%d年%d月" % (obj.year, obj.month)

    def staff_name(self, obj):
        return "%s (%s)" % (obj.name, obj.staff.identifier)

    def last_month_reach_percent(self, obj):
        return "%d%%" % (obj.last_month_reach * 100)

    def current_month_reach_percent(self, obj):
        return "%d%%" % (obj.current_month_reach * 100)

    def sfa_reach_percent(self, obj):
        return "%d%%" % (obj.sfa_reach * 100)

    def total_bonus(self, obj):
        return "%0.2f" % (obj.sale_bonus + obj.exam_bonus)

    date.short_description = '日期'
    staff_name.short_description = '姓名'
    last_month_reach_percent.short_description = '上月客户达成率'
    current_month_reach_percent.short_description = '本月客户达成率'
    sfa_reach_percent.short_description = 'SFA回单达成系数占比'
    total_bonus.short_description = '奖金合计'


class DataImportAdmin(admin.ModelAdmin):
    list_display = ('date', 'create_time')

    def date(self, obj):
        return "%d年%d月" % (obj.year, obj.month)

    date.short_description = '数据日期'

admin.site.empty_value_display = '无'
admin.site.register(Area, AreaAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobMatch, JobMatchAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientTarget, ClientTargetAdmin)
admin.site.register(StaffTarget, StaffTargetAdmin)
admin.site.register(BonusHistory, BonusHistoryAdmin)
admin.site.register(DataImport, DataImportAdmin)
