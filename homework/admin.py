from django.contrib import admin
from .models import *

# admin.site.register(HW)
# admin.site.register(HWResult)
admin.site.register(HWType)
# admin.site.register(Task)
# admin.site.register(Answer)


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(HW)
class HWAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(HWResult)
class HWResultAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]