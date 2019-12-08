from django.contrib import admin
from .forms import *
from .models import *


class CourseSubscribeInline(admin.TabularInline):
    model = CourseSubscribe


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ['teacher']
    inlines = [
        CourseSubscribeInline,
    ]

    def get_queryset(self, request):
        qs = super(CourseAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(teacher=request.user)

    def get_fields(self, request, obj=None):
        fields = list(super(CourseAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if obj is None:
            exclude_set.add('teacher')
        return [f for f in fields if f not in exclude_set]

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.teacher = request.user
        super().save_model(request, obj, form, change)
