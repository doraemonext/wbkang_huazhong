# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Area(MPTTModel):
    """
    地区 Model
    """
    parent = TreeForeignKey('self', verbose_name='父地区', null=True, blank=True, related_name='children', db_index=True)
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


class Staff(models.Model):
    """
    员工 Model
    """
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER = (
        (GENDER_MALE, '男'),
        (GENDER_FEMALE, '女'),
    )

    STATUS_ACTIVE = 0
    STATUS_INACTIVE = 1
    STATUS = (
        (STATUS_ACTIVE, '在职'),
        (STATUS_INACTIVE, '离职'),
    )
    STATUS_TRIAL = 2

    identifier = models.CharField('员工号', max_length=100)
    password = models.CharField('密码', max_length=64)
    name = models.CharField('姓名', max_length=100)
    gender = models.IntegerField('性别', choices=GENDER)
    department = models.CharField('部门', max_length=100)
    job = models.ForeignKey(Job, verbose_name='岗位')
    area = TreeForeignKey(Area, verbose_name='地区')
    entry_date = models.DateField('入职日期')
    cost_center = models.CharField('成本中心', max_length=100)
    department_desc = models.CharField('部门描述', max_length=200)
    cost_center_number = models.CharField('成本中心码', max_length=100)
    status = models.IntegerField('员工状态', choices=STATUS)

    def __unicode__(self):
        return self.name + ' (' + self.identifier + ')'

    def get_status(self):
        if self.status == self.STATUS_ACTIVE:
            if (datetime.date.today() - self.entry_date).days > 6 * 30:
                return self.STATUS_ACTIVE
            else:
                return self.STATUS_TRIAL
        else:
            return self.STATUS_INACTIVE

    class Meta:
        db_table = 'perf_staff'
        verbose_name = '员工管理'
        verbose_name_plural = '员工管理'
        ordering = ['id']
