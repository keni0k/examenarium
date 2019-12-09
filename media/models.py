from django.db import models
from main.models import User


class Catalog(models.Model):
    class Meta:
        verbose_name = 'Директория'
        verbose_name_plural = 'Директории'
    name = models.CharField(max_length=100, verbose_name='Название директории', default='')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Наддиректория')

    def __str__(self):
        if self.parent is not None and self.parent != self:
            return "%s/%s" % (self.parent, self.name)
        else:
            return "%s" % self.name


class Image(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
    uploaded = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, verbose_name='Описание фото', blank=True)
    url = models.URLField(verbose_name='Ссылка на фото')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False, verbose_name='Загрузил')
    dir = models.ForeignKey(Catalog, verbose_name='Директория', on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        if len(self.name) > 0:
            return "%s/%s" % (self.dir, self.name)
        else:
            return "%s/%s" % (self.dir, "БЕЗ ИМЕНИ")


class Video(models.Model):
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
    uploaded = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, verbose_name='Название видео')
    url = models.URLField(verbose_name='Ссылка (youtube)')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False, verbose_name='Загрузил')
    dir = models.ForeignKey(Catalog, verbose_name='Директория', on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        if len(self.name) > 0:
            return "%s/%s" % (self.dir, self.name)
        else:
            return "%s/%s" % (self.dir, "БЕЗ ИМЕНИ")
