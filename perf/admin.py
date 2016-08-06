# -*- coding: utf-8 -*-

from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from perf.models import Area


class AreaAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('name', 'weight')

    sortable = 'order'

admin.site.register(Area, AreaAdmin)
