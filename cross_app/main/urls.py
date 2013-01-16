from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'cross_app.main.views.test'),
#    (r'^ajax_load_match_select/$', 'cross_app.main.views.load_match_select'),

    (r'^ajax_load_(?P<view_name>[^/]+)/$', 'cross_app.main.views.load_view'), # TODO: murat - parametreyi nasil okuyacagini bul.


)
