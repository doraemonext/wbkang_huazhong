# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Area(MPTTModel):
    """
    地区 Model
    """
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    name = models.CharField('名称', max_length=100)
    weight = models.FloatField('地区权数', blank=True, null=True)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        res = self.name
        if self.weight:
            res += ' (' + str(self.weight) + ')'
        return res

    class MPTTMeta:
        order_insertion_by = ['order']

    def save(self, *args, **kwargs):
        super(Area, self).save(*args, **kwargs)
        Area.objects.rebuild()

