from django.contrib import admin
from .models import *

admin.site.register(HWType)


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(HW)
class HWAdmin(admin.ModelAdmin):
    readonly_fields = ['teacher', 'course']
    inlines = [
        TaskInline,
    ]

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

    # def get_queryset(self, request):
    #     qs = super(HWResultAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(Answer.objects.get(result=self)[0].current_task.current_work.teacher)