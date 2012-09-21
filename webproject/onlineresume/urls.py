# -*- coding: utf-8 *-*
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'onlineresume.views.curriculum', name='home'),
    url(r'^contact/$', 'onlineresume.views.contact', name='contact'),
    url(r'^print_as_pdf/$', 'onlineresume.views.print_as_pdf',
        name='print_as_pdf'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),

)
