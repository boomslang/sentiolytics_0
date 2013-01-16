from django.conf.urls.defaults import patterns, include, url
from settings import DOCUMENT_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sentiolytics.views.home', name='home'),
    # url(r'^sentiolytics/', include('sentiolytics.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^', include('main.urls')),

    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': '%s' % DOCUMENT_ROOT, 'show_indexes': True}),
#    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),

)
