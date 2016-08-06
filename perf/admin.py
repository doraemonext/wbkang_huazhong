# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from perf.models import Area, Job


class AreaAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'weight')

    sortable = 'order'


class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'bonus_base', 'job_weight', 'sale_target_percent', 'exam_target_percent', 'profit_target_percent')

    def sale_target_percent(self, obj):
        return "%d%%" % (obj.sale_target * 100)

    def exam_target_percent(self, obj):
        return "%d%%" % (obj.exam_target * 100)

    def profit_target_percent(self, obj):
        return "%d%%" % (obj.profit_target * 100)

    sale_target_percent.short_description = '销售指标'
    exam_target_percent.short_description = '考核指标'
    profit_target_percent.short_description = '利润达成指标'


admin.site.register(Area, AreaAdmin)
admin.site.register(Job, JobAdmin)
