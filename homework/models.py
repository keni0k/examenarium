from django.db import models


class Task(models.Model):
    from django.contrib.auth.models import User  # Required to assign User as a borrower
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, help_text='Название задания')
    text = models.CharField(max_length=500, help_text='Описание задания')
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=True)
    deadline = models.DateTimeField(help_text='Дедлайн')