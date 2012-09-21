# -*- coding: utf-8 *-*
from django.db import models
from django.utils.translation import ugettext_lazy as _

from curriculumvitae import models as cv_models


class Style(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Styles")

    def __unicode__(self):
        return self.name


class Person(cv_models.Person):
    """Extend CV Person to add the selected styles"""

    curriculum_vitae_style = \
        models.ForeignKey(Style,
                          verbose_name=_("Curriculum Vitae Style"))
