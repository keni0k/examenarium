from django.apps import AppConfig


class CourseConfig(AppConfig):
    name = 'course'
    verbose_name = 'Курсы'


class HWConfig(AppConfig):
    name = 'homework'
    verbose_name = 'Домашняя работа'


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Пользователи'


class MediaConfig(AppConfig):
    name = 'media'
    verbose_name = 'Медиа'


class SwingTimeConfig(AppConfig):
    name = 'swingtime'
    verbose_name = 'Календарь'
    icon_name = 'date_range'

