# -*- coding: utf-8 *-*
from django.contrib import admin

from curriculumvitae.models import Person, ExperienceGroup, ExperienceItem, \
    LineItem


class ExperienceItemInline(admin.TabularInline):
    model = ExperienceItem


class LineItemInline(admin.TabularInline):
    model = LineItem


class ExperienceAdmin(admin.ModelAdmin):
    inlines = [
        LineItemInline
    ]
    list_display = \
        ["experience_type", "title", "start_date", "completion_date", ]


class ExperienceGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

admin.site.register(Person)
admin.site.register(ExperienceGroup, ExperienceGroupAdmin)
admin.site.register(ExperienceItem, ExperienceAdmin)
