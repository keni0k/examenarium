from django.db import models


class Catalog(models.Model):
    class Meta:
        verbose_name = 'Директория'
        verbose_name_plural = 'Директории'
    name = models.CharField(max_length=100, help_text='Название директории', default='')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, help_text='Наддиректория')

    def __str__(self):
        if self.parent is not None and self.parent != self:
            return "%s/%s" % (self.parent, self.name)
        else:
            return "%s" % self.name


class Image(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
    from django.contrib.auth.models import User
    uploaded = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, help_text='Описание фото', blank=True)
    url = models.URLField(help_text='Ссылка на фото')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)
    dir = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        if len(self.name) > 0:
            return "%s/%s" % (self.dir, self.name)
        else:
            return "%s/%s" % (self.dir, "БЕЗ ИМЕНИ")


class Video(models.Model):
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
    from django.contrib.auth.models import User
    uploaded = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, help_text='Название видео')
    url = models.URLField(help_text='Ссылка (youtube)')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=False)
    dir = models.ForeignKey(Catalog, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        if len(self.name) > 0:
            return "%s/%s" % (self.dir, self.name)
        else:
            return "%s/%s" % (self.dir, "БЕЗ ИМЕНИ")
