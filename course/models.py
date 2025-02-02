from datetime import date

from django.db import models
from main.models import User


class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    title = models.CharField(max_length=100, verbose_name='Название курса', default='')
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False, verbose_name='Преподаватель', related_name='teacher')

    def __str__(self):
        return "%s" % self.title


class MasterGroup(models.Model):
    class Meta:
        verbose_name = 'Мастер-группа'
        verbose_name_plural = 'Мастер-группы'
    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE, null=True, blank=False)
    curators = models.ManyToManyField(User, verbose_name='Кураторы', related_name='curators')


class MasterGroupSubscribe(models.Model):
    class Meta:
        verbose_name = 'Подписка на МГ'
        verbose_name_plural = 'Подписки на МГ'

    student = models.ForeignKey(User, verbose_name='Ученик', on_delete=models.CASCADE, null=True, blank=False)
    subscribed_until = models.DateField(auto_now_add=False, verbose_name='Подписка активна до')
    master_group = models.ForeignKey(MasterGroup, verbose_name='Мастер-группа', on_delete=models.CASCADE, null=True, blank=False)

    def is_active(self):
        return date.today() <= self.subscribed_until

    def __str__(self):
        if self.is_active():
            return 'Подписка "%s" на курс "%s" активна' % (self.student, self.master_group)
        return 'Подписка "%s" на курс "%s" истекла' % (self.student, self.master_group)
