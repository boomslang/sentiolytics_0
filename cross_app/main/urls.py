from django.conf.urls.defaults import *

urlpatterns = patterns('',

#    (r'^ajax_load_match_select/$', 'cross_app.main.views.load_match_select'),

    (r'^ajax_load_leagues/$', 'cross_app.main.views.ajax_load_leagues'),
    (r'^ajax_load_matches/$', 'cross_app.main.views.ajax_load_matches'),
    (r'^ajax_add_to_session/$', 'cross_app.main.views.ajax_add_to_session'),
    (r'^ajax_mw_load_score/$', 'cross_app.main.views.ajax_mw_load_score'),


    (r'^ajax_load_mw_tab_(?P<tab_name>[^/]+)/$', 'cross_app.main.views.ajax_load_mw_tab'),

    (r'^ajax_load_(?P<view_name>[^/]+)/$', 'cross_app.main.views.ajax_load_view'),

    (r'^$', 'cross_app.main.views.test'),
)
