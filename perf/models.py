# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
import os
import xlrd
from django.conf import settings
from django.db import models
from django.db.models import signals
from django.core.exceptions import ValidationError
from django.db import transaction
from mptt.models import MPTTModel, TreeForeignKey


class Area(MPTTModel):
    """
    地区 Model
    """
    parent = TreeForeignKey('self', verbose_name='父地区', null=True, blank=True, related_name='children', db_index=True)
    name = models.CharField('名称', max_length=100)
    weight = models.FloatField('地区权数', blank=True, null=True)

    def __unicode__(self):
        res = self.name
        if self.weight:
            res += ' (' + str(self.weight) + ')'
        return res

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'perf_area'
        verbose_name = '地区管理'
        verbose_name_plural = '地区管理'


class Job(models.Model):
    """
    岗位 Model
    """
    name = models.CharField('名称', max_length=100)
    bonus_base = models.FloatField('奖金基数(元)')
    job_weight = models.FloatField('职务权数')
    sale_target = models.FloatField('销售指标', help_text='取值范围 0 - 1')
    exam_target = models.FloatField('考核指标', help_text='取值范围 0 - 1')
    profit_target = models.FloatField('利润达成指标', default=0, help_text='取值范围 0 - 1')
    has_trial = models.BooleanField('存在试用期', default=False)
    trial_days = models.IntegerField('试用期时长(天)', help_text='仅在存在试用期时有效', default=180)
    trial_sale_target = models.FloatField('试用期销售指标', help_text='仅在存在试用期时有效, 取值范围 0 - 1', default=0)
    trial_exam_target = models.FloatField('试用期考核指标', help_text='仅在存在试用期时有效, 取值范围 0 - 1', default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'perf_job'
        verbose_name = '岗位管理'
        verbose_name_plural = '岗位管理'
        ordering = ['-id']


class JobMatch(models.Model):
    """
    岗位对应名称 Model
    """
    name = models.CharField('详细名称', max_length=100, unique=True)
    job = models.ForeignKey(Job, verbose_name='对应岗位')

    def __unicode__(self):
        return self.name + " (" + self.job.name + ")"

    class Meta:
        db_table = 'perf_job_match'
        verbose_name = '岗位名称管理'
        verbose_name_plural = '岗位名称管理'
        ordering = ['name']


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

    identifier = models.CharField('员工号', max_length=100, unique=True)
    password = models.CharField('密码', max_length=64)
    name = models.CharField('姓名', max_length=100)
    gender = models.IntegerField('性别', choices=GENDER)
    department = models.CharField('部门', max_length=100)
    job = models.ForeignKey(Job, verbose_name='岗位')
    job_name = models.CharField('岗位名称', max_length=100, blank=True)
    area = TreeForeignKey(Area, verbose_name='地区')
    entry_date = models.DateField('入职日期')
    cost_center = models.CharField('成本中心', max_length=100)
    department_desc = models.CharField('部门描述', max_length=200)
    cost_center_number = models.CharField('成本中心码', max_length=100)
    status = models.IntegerField('员工状态', choices=STATUS)
    openid = models.CharField('微信绑定ID', max_length=255, default='', blank=True, help_text='修改此处将导致原绑定无效')

    def __unicode__(self):
        return self.name + ' (' + self.identifier + ')'

    def clean(self):
        if len(self.openid) > 0:
            staff = Staff.objects.filter(openid=self.openid)
            if staff.exists() and staff[0].identifier != self.identifier:
                raise ValidationError('该微信绑定ID已经用于用户 %s (%s)' % (staff[0].name, staff[0].identifier))

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
    name = models.CharField('姓名', max_length=100, default='')
    job_name = models.CharField('岗位名称', max_length=100, default='')
    bonus_base = models.FloatField('奖金基数(元)', default=0)
    job_weight = models.FloatField('职务权数', default=0)
    area_weight = models.FloatField('地区权数', default=0)
    last_month_reach = models.FloatField('上月客户达成率', help_text='取值范围 0 - 1')
    current_month_reach = models.FloatField('本月客户达成率', help_text='取值范围 0 - 1')
    sfa_reach = models.FloatField('SFA回单达成系数占比', help_text='取值范围 0 - 1')
    sale_bonus = models.FloatField('个人销售奖金')
    exam_bonus = models.FloatField('个人考核奖金')

    def clean(self):
        if self.year < 1900 or self.year > 2100 or self.month < 1 or self.month > 12:
            raise ValidationError('年月不合法')
        if self.pk is None and BonusHistory.objects.filter(year=self.year, month=self.month, staff=self.staff).exists():
            raise ValidationError('员工 %s 的 %d 年 %d 月奖金历史记录已存在, 请返回上一页搜索' % (self.staff, self.year, self.month))

    def save(self, *args, **kwargs):
        if self.staff is not None:
            self.name = self.staff.name
            self.job_name = self.staff.job.name
            self.bonus_base = self.staff.job.bonus_base
            self.job_weight = self.staff.job.job_weight
            self.area_weight = self.staff.area.weight
        super(BonusHistory, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s %d-%d" % (self.staff, self.year, self.month)

    class Meta:
        db_table = 'perf_bonus_history'
        verbose_name = '奖金历史记录'
        verbose_name_plural = '奖金历史记录'
        ordering = ['-id']


class StaffDataImport(models.Model):
    """
    导入数据 Model
    """
    year = models.IntegerField("年")
    month = models.IntegerField("月")
    file = models.FileField("Excel 文件")
    imported = models.BooleanField("是否成功导入", default=False)
    message = models.TextField("说明信息", default='')
    create_time = models.DateTimeField("上传日期", auto_now_add=True)

    def __unicode__(self):
        return "%d-%d" % (self.year, self.month)

    class Meta:
        db_table = 'perf_staff_data_import'
        verbose_name = '员工信息导入'
        verbose_name_plural = '员工信息导入'
        ordering = ['-year', '-month']

    def save(self, *args, **kwargs):
        return super(StaffDataImport, self).save(*args, **kwargs)


def import_staff_data(sender, instance, created, **kwargs):
    if not created:
        return

    # filepath = os.path.join(settings.BASE_DIR, 'media', instance.file.name)
    book = xlrd.open_workbook(instance.file.path)
    length = len(book.sheet_names())
    if length < 1:
        instance.imported = False
        instance.message = "至少需要一个 Sheet"
        instance.save()
        return

    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    if nrows <= 2:
        instance.imported = False
        instance.message = "数据文件不足 2 行"
        instance.save()
        return
    if ncols != 11:
        instance.imported = False
        instance.message = "数据文件列数不为 10"
        instance.save()
        return

    sid = transaction.savepoint()
    for row in range(2, nrows):
        identifier = str(int(sheet.cell_value(row, 1)))
        name = sheet.cell_value(row, 2)
        gender = sheet.cell_value(row, 3)
        department = sheet.cell_value(row, 4)
        job_name = sheet.cell_value(row, 5)
        entry_date_tmp = xlrd.xldate_as_tuple(sheet.cell_value(row, 6), book.datemode)[:3]
        entry_date = datetime.date(*entry_date_tmp).strftime("%Y-%m-%d")
        cost_center = sheet.cell_value(row, 7)
        department_desc = sheet.cell_value(row, 8)
        cost_center_number = sheet.cell_value(row, 9)
        area_name = sheet.cell_value(row, 10)

        job_name_model = JobMatch.objects.filter(name=job_name)
        if not job_name_model.exists():
            transaction.savepoint_rollback(sid)
            instance.imported = False
            instance.message = "F%d 单元格数据错误, 未找到 %s 岗位名称的对应关系" % (row+1, job_name)
            instance.save()
            return
        job = job_name_model[0].job

        area_model = Area.objects.filter(name=area_name)
        if not area_model.exists():
            transaction.savepoint_rollback(sid)
            instance.imported = False
            instance.message = "K%d 单元格数据错误, 未找到名称为 %s 的地区" % (row+1, area_name)
            instance.save()
            return
        area = area_model[0]

        Staff.objects.get_or_create(
            identifier=identifier,
            name=name,
            password="123456",
            gender=Staff.GENDER_MALE if gender == "男" else Staff.GENDER_FEMALE,
            area=area,
            department=department,
            job=job,
            job_name=job_name,
            entry_date=entry_date,
            cost_center=cost_center,
            department_desc=department_desc,
            cost_center_number=cost_center_number,
            status=Staff.STATUS_ACTIVE,
        )

    transaction.savepoint_commit(sid)
    instance.imported = True
    instance.message = "导入成功, 共导入 %d 个员工数据" % (nrows - 2)
    instance.save()

signals.post_save.connect(import_staff_data, sender=StaffDataImport)
