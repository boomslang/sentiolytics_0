from django.conf.urls.defaults import *

urlpatterns = patterns('',

#    (r'^ajax_load_match_select/$', 'cross_app.main.views.load_match_select'),

    (r'^ajax_load_leagues/$', 'cross_app.main.views.ajax_load_leagues'),
    (r'^ajax_load_(?P<view_name>[^/]+)/$', 'cross_app.main.views.ajax_load_view'),

    (r'^$', 'cross_app.main.views.test'),
)
