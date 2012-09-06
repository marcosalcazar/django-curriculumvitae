# -*- coding: utf-8 *-*
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'curriculumvitae.views.curriculum', name='home'),
    url(r'^contact/$', 'curriculumvitae.views.contact', name='contact'),
    # url(r'^curriculumvitae/', include('curriculumvitae.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),

)
