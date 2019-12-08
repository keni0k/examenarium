from django.db import models
from media.models import Image
from django.contrib.auth.models import User


class HWType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус задания', null=True, blank=False)

    def __str__(self):
        return "%s" % self.name


class HW(models.Model):
    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'
    title = models.CharField(max_length=100, verbose_name='Название работы', null=True, blank=False)
    description = models.CharField(max_length=500, verbose_name='Описание работы', null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    deadline = models.DateTimeField(verbose_name='Дедлайн', null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.title, self.teacher)


class Task(models.Model):
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    title = models.CharField(max_length=100, verbose_name='Название задания', null=True, blank=False)
    description = models.CharField(max_length=500, verbose_name='Описание задания', null=True, blank=False)
    support_image = models.ForeignKey(Image, on_delete=models.PROTECT, verbose_name='Прикрепить изображение', null=True, blank=True)
    current_work = models.ForeignKey(HW, on_delete=models.PROTECT, verbose_name='К какому ДЗ относится', null=False, blank=False)
    right_answer = models.CharField(max_length=500, verbose_name='Правильный ответ', null=True, blank=True)
    max_result = models.IntegerField(verbose_name='Максимальный балл', blank=False)

    def __str__(self):
        return "№%d - %s (%s)" % (self.id, self.title, self.current_work.title)


class HWResult(models.Model):
    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
    finish = models.DateField(auto_now_add=True)
    result = models.ForeignKey(HWType, on_delete=models.PROTECT, null=False, blank=False)
    student = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return "Работа %s имеет статус %s" % (self.student, self.result)


class Answer(models.Model):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
    current_task = models.ForeignKey(Task, on_delete=models.PROTECT, null=False, blank=False)
    your_case = models.CharField(max_length=1000, verbose_name='Ваш ответ', null=True, blank=False)  # Стоит изменить на TextField
    result = models.ForeignKey(HWResult, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return 'Ответ "%s" на задачу "%s" с правильным ответом "%s"' \
               % (self.your_case, self.current_task.title, self.current_task.right_answer)
