from django.contrib import admin
from .forms import *


class VideoInline(admin.TabularInline):
    model = Video
    readonly_fields = ["owner"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    form = VideoForm
    list_display = ('__str__', 'owner')
    list_filter = ('dir', 'owner')

    def get_queryset(self, request):
        qs = super(VideoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['owner']
        return self.readonly_fields


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    inlines = [
        VideoInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
