from django.contrib import admin
from .models import *
from .forms import *

class VideoInline(admin.TabularInline):
    model = Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    # form = VideoForm

    def get_readonly_fields(self, request, obj=None):
        if obj:  # when editing an object
            return ['owner']
        return self.readonly_fields


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    inlines = [
        VideoInline,
    ]
