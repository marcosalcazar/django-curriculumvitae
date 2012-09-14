# -*- coding: utf-8 *-*
from transmeta import TransMeta

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Style(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))

    class Meta:
        verbose_name_plural = _("Styles")

    def __unicode__(self):
        return self.name


class Person(models.Model):
    __metaclass__ = TransMeta

    first_name = models.CharField(max_length=255,
                                  verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255,
                                 verbose_name=_("Last Name"))
    short_description = \
        models.CharField(max_length=255, verbose_name=_("Short Description"))
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    mugshot = models.ImageField(upload_to='mugshots',
                                help_text=_("A squared one is prefered"))
    curriculum_vitae_style = \
        models.ForeignKey(Style,
                          verbose_name=_("Curriculum Vitae Style"))

    class Meta:
        verbose_name_plural = _("Personal Info")
        translate = ('short_description', )

    def full_name(self):
        return " ".join([self.first_name, self.last_name])

    def __unicode__(self):
        return self.full_name()


class ExperienceGroup(models.Model):
    __metaclass__ = TransMeta

    person = models.ForeignKey(Person, related_name='experiences_groups',
                               verbose_name=_('Person'))
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    order = models.IntegerField()

    class Meta:
        verbose_name_plural = _("Experience Groups")
        ordering = ('order',)
        translate = ('name',)

    def __unicode__(self):
        return self.name


class ExperienceItem(models.Model):
    __metaclass__ = TransMeta

    experience_type = models.ForeignKey(ExperienceGroup,
                                        related_name='experiences',
                                        verbose_name=_('Experience Type'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    subtitle = models.CharField(max_length=255,
                                verbose_name=_('Subtitle'), blank=True)
    url = models.URLField('URL', verify_exists=False, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True,
                                verbose_name=_('Location'))
    description = models.TextField(verbose_name=_('Description'),
                                   null=True, blank=True)
    start_date = models.DateField(verbose_name=_('Start Date'),
                                  null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True,
                                       verbose_name=_('Completion Date'))

    def __unicode__(self):
        return u"%s at %s" % (self.experience_type, self.title)

    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")
        ordering = ("start_date", "completion_date", )
        translate = ("title", "subtitle", "description", )


class LineItem(models.Model):
    __metaclass__ = TransMeta

    experience = models.ForeignKey(ExperienceItem, related_name="items")
    url = models.URLField('URL', verify_exists=False, blank=True, null=True)
    details = models.CharField(max_length=255, verbose_name=_('Details'))

    class Meta:
        translate = ("details", )
