# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
from django.db import models
from django.core.exceptions import ValidationError
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
    has_trial = models.BooleanField('存在试用期', default=False)
    trial_days = models.IntegerField('试用期时长(天)', help_text='仅在存在试用期时有效', default=180)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'perf_job'
        verbose_name = '岗位管理'
        verbose_name_plural = '岗位管理'
        ordering = ['-id']


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
            if self.job.has_trial and (datetime.date.today() - self.entry_date).days <= self.job.trial_days:
                return self.STATUS_TRIAL
            else:
                return self.STATUS_ACTIVE
        else:
            return self.STATUS_INACTIVE

    class Meta:
        db_table = 'perf_staff'
        verbose_name = '员工管理'
        verbose_name_plural = '员工管理'
        ordering = ['-id']


class Client(models.Model):
    """
    客户 Model
    """
    identifier = models.CharField('客户代码', max_length=100)
    name = models.CharField('客户名称', max_length=100)

    def __unicode__(self):
        return self.name + ' (' + self.identifier + ')'

    class Meta:
        db_table = 'perf_client'
        verbose_name = '客户信息管理'
        verbose_name_plural = '客户信息管理'
        ordering = ['-id']


class ClientTarget(models.Model):
    """
    客户目标 Model
    """
    client = models.ForeignKey(Client, verbose_name='客户')
    year = models.IntegerField("年")
    month = models.IntegerField("月")
    target = models.FloatField("客户目标金额(元)")

    def clean(self):
        if self.year < 1900 or self.year > 2100 or self.month < 1 or self.month > 12:
            raise ValidationError('年月不合法')
        if self.pk is None and ClientTarget.objects.filter(client=self.client, year=self.year, month=self.month).exists():
            raise ValidationError('客户 %s 的 %d 年 %d 月目标已存在, 请返回上一页搜索' % (self.client, self.year, self.month))

    def __unicode__(self):
        return "%s(%s) %d-%d" % (self.client.name, self.client.identifier, self.year, self.month)

    class Meta:
        db_table = 'perf_client_target'
        verbose_name = '客户目标管理'
        verbose_name_plural = '客户目标管理'
        ordering = ['-year', '-month', '-id']


class StaffTarget(models.Model):
    """
    员工目标管理 Model
    """
    staff = models.ForeignKey(Staff, verbose_name='员工')
    client_target = models.ForeignKey(ClientTarget, verbose_name='客户目标')
    target = models.FloatField('个人目标(元)')

    def __unicode__(self):
        return self.staff.name + ' - ' + self.client_target.__unicode__()

    class Meta:
        db_table = 'perf_staff_target'
        verbose_name = '员工目标管理'
        verbose_name_plural = '员工目标管理 '
        ordering = ['-id']


class BonusHistory(models.Model):
    """
    奖金历史记录 Model
    """
    year = models.IntegerField('年')
    month = models.IntegerField('月')
    staff = models.ForeignKey(Staff, verbose_name='员工')
    last_month_reach = models.FloatField('上月客户达成率')
    current_month_reach = models.FloatField('本月客户达成率')
    sfa_reach = models.FloatField('SFA回单达成系数占比')
    sale_bonus = models.FloatField('个人销售奖金')
    exam_bonus = models.FloatField('个人考核奖金')

    def clean(self):
        if self.year < 1900 or self.year > 2100 or self.month < 1 or self.month > 12:
            raise ValidationError('年月不合法')
        if self.pk is None and BonusHistory.objects.filter(year=self.year, month=self.month, staff=self.staff).exists():
            raise ValidationError('员工 %s 的 %d 年 %d 月奖金历史记录已存在, 请返回上一页搜索' % (self.staff, self.year, self.month))

    def __unicode__(self):
        return "%s %d-%d" % (self.staff, self.year, self.month)

    class Meta:
        db_table = 'perf_bonus_history'
        verbose_name = '奖金历史记录'
        verbose_name_plural = '奖金历史记录'
        ordering = ['-id']
