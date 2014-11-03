
import requests
import json
from datetime import datetime

__author__ = 'Jason Thomas'


class WhiskerBoardApi(object):

    default_protocol = 'http'
    default_host = 'localhost'
    default_port = '8000'
    default_user = 'api'
    default_password = 'digest'
    default_api = '/api/v1'

    def __init__(self, protocol=default_protocol, host=default_host,
                 port=default_port, api=default_api, user=default_user,
                 password=default_password):

        self.user = user
        self.password = password
        self.api_endpoint = '{0}://{1}:{2}{3}'.format(protocol, host,
                                                      port, api)

        self.headers = {
            'Content-type': 'application/json',
            'Accept': '*/*',
            'Authorization': '{0} {1}:{2}'.format('ApiKey', self.user,
                                                  self.password)
        }

    def get_status_uri(self, slug):

        status_endpoint = '{0}/statuses/?slug={1}'.format(self.api_endpoint,
                                                          slug)
        r = requests.get(status_endpoint, headers=self.headers)
        return r.json()['objects'][0]['resource_uri']

    def get_service_uri(self, slug):
        service_endpoint = '{0}/services/?slug={1}'.format(self.api_endpoint,
                                                           slug)
        r = requests.get(service_endpoint, headers=self.headers)
        return r.json()['objects'][0]['resource_uri']

    def update_status(self, status, message, service):

        # getting uri
        status = status.lower()
        service = service.lower()

        status_uri = self.get_status_uri(status)
        service_uri = self.get_service_uri(service)

        events_endpoint = '{0}/events/'.format(self.api_endpoint)

        params = {
            'informational': False,
            'message': '{0}'.format(message),
            'service': '{0}'.format(service_uri),
            'start': '{0}'.format(datetime.now()),
            'status': '{0}'.format(status_uri),
        }
        print params

        r = requests.post(events_endpoint, data=json.dumps(params),
                          headers=self.headers)

        return r
