from django.contrib import admin
from .models import *


@admin.register(HWType)
class HWTypeAdmin(admin.ModelAdmin):
    icon_name = 'turned_in'


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(HW)
class HWAdmin(admin.ModelAdmin):
    readonly_fields = ['teacher', 'course']
    inlines = [
        TaskInline,
    ]
    icon_name = 'home'

    def get_fields(self, request, obj=None):
        fields = list(super(HWAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if obj is None:  # obj will be None on the add page, and something on change pages
            exclude_set.add('teacher')
            exclude_set.add('course')
        return [f for f in fields if f not in exclude_set]

    def get_queryset(self, request):
        qs = super(HWAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(teacher=request.user)

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.teacher = request.user
        super().save_model(request, obj, form, change)


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(HWResult)
class HWResultAdmin(admin.ModelAdmin):
    readonly_fields = ["student"]
    inlines = [
        AnswerInline,
    ]
    icon_name = 'event_available'

    def get_fields(self, request, obj=None):
        fields = list(super(HWResultAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if obj is None:  # obj will be None on the add page, and something on change pages
            exclude_set.add('student')
        return [f for f in fields if f not in exclude_set]

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.student = request.user
        super().save_model(request, obj, form, change)
