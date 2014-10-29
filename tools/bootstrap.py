#!/usr/bin/python -tt
import httplib
import json
import sys

# basic bootstrap of our services via the API

# TODO load yaml
# TODO don't hard-code category URIs
# FIXME setting site properties cannot be done by the API yet


class Api():
    @staticmethod
    def api_auth(user, key):
        return 'ApiKey {}:{}'.format(user, key)

    def __init__(self, user, key):
        self.conn = httplib.HTTPConnection('localhost', '8000')
        self.conn.set_debuglevel(1)
        self.headers = {
            'Content-type': 'application/json',
            'Authorization': Api.api_auth(user, key),
            'Accept': '*/*'
        }

    def post(self, endpoint, params):
        params = json.dumps(params)
        self.conn.request('POST', endpoint, params, self.headers)
        response = self.conn.getresponse()
        data = response.read()
        print(response.status, response.reason)
        print(data)

# set categories / services
fx = {
    "name": "Firefox Services",
    "slug": "firefox-services",
    "description": "Services supporting the Firefox browser"
}

fx_services = [
    {
        "name": "Firefox Accounts",
        "slug": "fxa",
        "description": "The Firefox Accounts Service",
        "category": "/api/v1/categories/1/",
    },
    {
        "name": "Firefox Hello",
        "slug": "fx-hello",
        "description": "The Firefox Hello Service",
        "category": "/api/v1/categories/1/",
    },
    {
        "name": "Firefox Sync",
        "slug": "fx-sync",
        "description": "The Firefox Sync Service",
        "category": "/api/v1/categories/1/",
    }
]

mz = {
    "name": "Mozilla Services",
    "slug": "mozilla-services",
    "description": "Other Mozilla services"
}

mz_services = [
    {
        "name": "APK Factory",
        "slug": "apk",
        "description": "The APK Factory Service",
        "category": "/api/v1/categories/2/",
    },
    {
        "name": "Mozilla Location Service",
        "slug": "location",
        "description": "The Mozilla Location Service",
        "category": "/api/v1/categories/2/",
    }
]

if __name__ == "__main__":
    api = Api(sys.argv[1], sys.argv[2])

    api.post('/api/v1/categories/', fx)
    api.post('/api/v1/categories/', mz)

    for svc in fx_services + mz_services:
        api.post('/api/v1/services/', svc)
