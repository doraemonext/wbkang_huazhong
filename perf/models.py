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

    class Meta:
        db_table = 'perf_area'
        verbose_name = '地区管理'
        verbose_name_plural = '地区管理'

    def save(self, *args, **kwargs):
        super(Area, self).save(*args, **kwargs)
        Area.objects.rebuild()


class Job(models.Model):
    """
    岗位 Model
    """
    name = models.CharField('名称', max_length=100)
    bonus_base = models.FloatField('奖金基数')
    job_weight = models.FloatField('职务权数')
    sale_target = models.FloatField('销售指标')
    exam_target = models.FloatField('考核指标')
    profit_target = models.FloatField('利润达成指标', default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'perf_job'
        verbose_name = '岗位管理'
        verbose_name_plural = '岗位管理'
        ordering = ['id']
