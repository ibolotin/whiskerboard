from board.models import Service, Status, Incident, Event
import datetime
from collections import OrderedDict
from django.views.generic import ListView, DetailView
from django.template import RequestContext
from django.db import models
from django.shortcuts import render_to_response, get_object_or_404
import calendar


class BoardMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BoardMixin, self).get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


def get_start_date(days=7):
    return datetime.date.today() - datetime.timedelta(days=days)


def get_dates(days=7):
    base = datetime.datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0)
    print base
    dates = OrderedDict(
        (base - datetime.timedelta(days=x), []) for x in range(0, days))

    return dates


class IndexView(BoardMixin, ListView):
    context_object_name = 'services'
    queryset = Service.objects.all()
    template_name = 'board/index.html'

    def get_context_data(self, **kwargs):
        start_date = get_start_date(14)
        context = super(IndexView, self).get_context_data(**kwargs)
        context['default'] = Status.objects.default()
        # sqlite doesn't support DISTINCT ON
        # incidents = Incident.objects.filter(
        #     events__start__gte=start_date).distinct('name').order_by('-events')
        # It would probably be easier to denormalize incident start time
        incidents = Incident.objects.filter(
            events__start__gte=start_date).annotate(
                models.Max("events__start")).order_by('-events__start__max')
        dates = get_dates(14)

        # FIXME a correct top-level status for a service would be the "min" of
        # the most recent event for that service in each incident which
        # includes that service. Currently we are just using the status of
        # the latest event associated with the service.
        for incident in incidents:
            services = ", ".join(
                [svc.name for svc in Service.objects.filter(
                    events__incident=incident).distinct()])
            # this is probably bad style
            incident.services = services
            start = incident.events.order_by('start')[:1].get()
            end = incident.events.order_by('-start')[:1].get()
            # display an incident if either its starting or ending event fits
            # in the current time slice
            start_key = start.start.replace(
                hour=0, minute=0, second=0, microsecond=0)
            end_key = end.start.replace(
                hour=0, minute=0, second=0, microsecond=0)
            if start_key in dates:
                dates[start_key].append(incident)
            elif end_key in dates:
                dates[end_key].append(incident)

        context['dates'] = dates

        return context


class ServiceView(BoardMixin, DetailView):
    model = Service
    template_name = 'board/service_detail.html'

    def get(self, request, slug=None, days=30):
        start_date = get_start_date(days)
        data = get_object_or_404(self.model, slug=slug)

        incidents = Incident.objects.filter(
            events__start__gte=start_date,
            events__service__exact=data).annotate(
                models.Max("events__start")).order_by('-events__start__max')

        # this can be wrong if you've had an incident running for longer than
        # the time slice in question (you shouldn't)
        no_incidents = None
        if len(incidents) == 0:
            no_incidents = 'No events found.'

        dates = get_dates(days)
        for incident in incidents:
            services = ", ".join(
                [svc.name for svc in Service.objects.filter(
                    events__incident=incident).distinct()])
            # this is probably bad style
            incident.services = services
            # FIXME code duplication
            start = incident.events.order_by('start')[:1].get()
            end = incident.events.order_by('-start')[:1].get()
            # display an incident if either its starting or ending event fits
            # in the current time slice
            start_key = start.start.replace(
                hour=0, minute=0, second=0, microsecond=0)
            end_key = end.start.replace(
                hour=0, minute=0, second=0, microsecond=0)
            if start_key in dates:
                dates[start_key].append(incident)
            elif end_key in dates:
                dates[end_key].append(incident)

        return render_to_response(self.template_name, {
            'service': data,
            'dates': dates,
            'no_incidents': no_incidents,
            'default': Status.objects.default()
        }, context_instance=RequestContext(request))


class IncidentView(BoardMixin, DetailView):
    model = Incident
    template_name = 'board/incident_detail.html'

    def get(self, request, slug=None):
        data = get_object_or_404(self.model, slug=slug)
        services = Service.objects.filter(
            events__incident=data).distinct()
        return render_to_response(self.template_name, {
            'incident': data,
            'services': services,
        }, context_instance=RequestContext(request))
