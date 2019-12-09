from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from swingtime.models import *


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    icon_name = 'label'
    list_display = ('label', 'abbr')


class OccurrenceInline(admin.TabularInline):
    model = Occurrence
    extra = 1


class EventNoteInline(GenericTabularInline):
    model = Note
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    icon_name = 'event'
    list_display = ('title', 'event_type', 'description')
    list_filter = ('event_type', )
    search_fields = ('title', 'description')
    inlines = [EventNoteInline, OccurrenceInline]
