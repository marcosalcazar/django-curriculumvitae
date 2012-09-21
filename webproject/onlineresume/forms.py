# -*- coding: utf-8 *-*
from django import forms
from django.forms.widgets import *
from django.utils.translation import ugettext_lazy as _

from captcha.fields import CaptchaField


class ContactForm(forms.Form):

    error_css_class = "error"

    name = forms.CharField(label=_(u'Name'))
    email = forms.EmailField(label=_(u'Email'))
    topic = forms.CharField(label=_(u'Topic'))
    message = forms.CharField(widget=Textarea(), label=_(u'Message'))
    captcha = CaptchaField()
