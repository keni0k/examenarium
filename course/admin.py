from django.contrib import admin
from django.db.models import Q
from .models import *


class MasterGroupInline(admin.TabularInline):
    model = MasterGroup


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [
        MasterGroupInline,
    ]
    icon_name = 'school'

    def get_queryset(self, request):
        qs = super(CourseAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Q(teacher=request.user))


class MasterGroupSubscribeInline(admin.TabularInline):
    model = MasterGroupSubscribe


@admin.register(MasterGroup)
class MGAdmin(admin.ModelAdmin):
    inlines = [
        MasterGroupSubscribeInline,
    ]
    icon_name = 'group'

    def get_queryset(self, request):
        qs = super(MGAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='Преподаватель').exists():
            return qs
        return qs.filter(Q(curators__in=[request.user]))
