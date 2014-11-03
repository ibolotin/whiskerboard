from board.models import Service, Status, Event
import datetime
from django.views.generic import ListView, DetailView
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import calendar


class BoardMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BoardMixin, self).get_context_data(**kwargs)
        context['statuses'] = Status.objects.all()
        return context


def get_start_date(days=7):
    return datetime.date.today() - datetime.timedelta(days=days)


class IndexView(BoardMixin, ListView):
    context_object_name = 'services'
    queryset = Service.objects.all()
    template_name = 'board/index.html'

    def get_context_data(self, **kwargs):
        start_date = get_start_date()

        context = super(IndexView, self).get_context_data(**kwargs)
        context['default'] = Status.objects.default()
        context['events'] = Event.objects.filter(start__gte=start_date).order_by('service', '-start')

        return context


class ServiceView(BoardMixin, DetailView):
    model = Service
    template_name = 'board/service_detail.html'

    def get(self, request, slug=None, days=30):

        data = get_object_or_404(self.model, slug=slug)
        start_date = get_start_date(days)
        events = data.events.filter(start__gte=start_date)

        no_events = None
        if len(events) == 0:
            no_events = 'No events found.'

        return render_to_response(self.template_name, {
            'service': data,
            'events': events,
            'no_events': no_events,
        }, context_instance=RequestContext(request))
