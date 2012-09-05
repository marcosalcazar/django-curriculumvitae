# -*- coding: utf-8 *-*
from django import forms
from django.forms.widgets import *
from django.utils.translation import ugettext as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'))
    email = forms.EmailField(label=_('Email'))
    topic = forms.CharField(label=_('Topic'))
    message = forms.CharField(widget=Textarea(), label=_('Message'))
