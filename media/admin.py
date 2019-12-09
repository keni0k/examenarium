from django.contrib import admin
from .forms import *


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    readonly_fields = ["owner"]
    list_display = ('__str__', 'owner')
    list_filter = ('dir', 'owner')
    icon_name = 'video_library'

    def get_queryset(self, request):
        qs = super(VideoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def get_fields(self, request, obj=None):
        fields = list(super(VideoAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if obj is None:
            exclude_set.add('owner')
        return [f for f in fields if f not in exclude_set]

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.owner = request.user
        super().save_model(request, obj, form, change)


class VideoInline(admin.TabularInline):
    model = Video
    readonly_fields = ["owner"]


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ["owner"]


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    inlines = [
        VideoInline, ImageInline
    ]
    icon_name = 'folder'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["owner"]
    icon_name = 'photo_library'

    def get_queryset(self, request):
        qs = super(ImageAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def get_fields(self, request, obj=None):
        fields = list(super(ImageAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if obj is None:
            exclude_set.add('owner')
        return [f for f in fields if f not in exclude_set]

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.owner = request.user
        super().save_model(request, obj, form, change)
