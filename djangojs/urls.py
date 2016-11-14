# -*- coding: utf-8 -*-
import sys

from os.path import join, isdir

from django.conf.urls import  url
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog

from djangojs.conf import settings
from djangojs.views import UrlsJsonView, ContextJsonView, JsInitView


urlpatterns = i18n_patterns(
    url(r'^init\.js$', JsInitView.as_view(), name='django_js_init'),
    url(r'^urls$', UrlsJsonView.as_view(), name='django_js_urls'),
    url(r'^context$', ContextJsonView.as_view(), name='django_js_context'),
    url(r'^translation$', JavaScriptCatalog.as_view(domain="django"), name='js_catalog'),
    prefix_default_language=False,
)
