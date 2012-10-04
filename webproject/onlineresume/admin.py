# -*- coding: utf-8 *-*
from django.contrib import admin

from curriculumvitae.models import Person as CVPerson
from onlineresume.models import Person, Style


admin.site.unregister(CVPerson)
admin.site.register(Person)
admin.site.register(Style)
