from django.conf.urls import patterns, include, url
from board.feeds import EventFeed
from board.views import (IndexView, ServiceView, IncidentView,
                         ContactBugzillaView)
from board.api import (ServiceResource, CategoryResource, StatusResource,
                       IncidentsResource, EventsResource, SiteResource)
from tastypie.api import Api
from django.contrib import admin

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(ServiceResource())
v1_api.register(CategoryResource())
v1_api.register(StatusResource())
v1_api.register(IncidentsResource())
v1_api.register(EventsResource())
v1_api.register(SiteResource())

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^services/(?P<slug>[-\w]+)$',
                           ServiceView.as_view(),
                           name='service'),
                       url(r'^incidents/(?P<slug>[-\w]+)$',
                           IncidentView.as_view(),
                           name='incident'),
                       url(r'^feed$', EventFeed(), name='feed'),
                       url(r'^api/', include(v1_api.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^contact$',
                           ContactBugzillaView.as_view(), name='contact'),
                       )
