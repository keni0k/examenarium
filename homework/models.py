from typing import Any

from django.db import models
from media.models import Image


class HWType(models.Model):
    name = models.CharField(max_length=100, help_text='Статус задания')


class Homework(models.Model):
    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'
    from django.contrib.auth.models import User
    name = models.CharField(max_length=100, help_text='Название работы')
    title = models.CharField(max_length=500, help_text='Описание работы')
    created = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=True)
    deadline = models.DateTimeField(help_text='Дедлайн')


class Task(models.Model):
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    from django.contrib.auth.models import User  # Required to assign User as a borrower
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, help_text='Название задания')
    text = models.CharField(max_length=500, help_text='Описание задания')
    support_image = models.ForeignKey(Image, on_delete=models.PROTECT, null=False, blank=True)
    current_work = models.ForeignKey(Homework, on_delete=models.PROTECT, null=False, blank=True)
    right_answer = models.CharField(max_length=500, help_text='Описание задания')
    max_result = models.IntegerField(help_text='Максимальное количество баллов за задание')


class HWResult(models.Model):
    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
    from django.contrib.auth.models import User
    finish = models.DateTimeField(auto_now_add=True)
    result = models.ForeignKey(HWType, on_delete=models.PROTECT, null=False, blank=True)
    student = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=True)


class Answer(models.Model):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    current_task = models.ForeignKey(Task, on_delete=models.PROTECT, null=False, blank=True)
    your_case = models.CharField(max_length=1000, help_text='Ваш ответ')  # Возможно стоит изменить на TextField
    result = models.ForeignKey(HWResult, on_delete=models.PROTECT, null=False, blank=True)
