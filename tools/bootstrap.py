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

    def use(self, method, endpoint, params):
        params = json.dumps(params)
        self.conn.request(method, endpoint, params, self.headers)
        response = self.conn.getresponse()
        data = response.read()
        print(response.status, response.reason)
        print(data)

    def post(self, endpoint, params):
        self.use("POST", endpoint, params)

    def put(self, endpoint, params):
        self.use("PUT", endpoint, params)


# set categories / services
mz = {
    "name": "Mozilla Services",
    "slug": "mozilla-services",
    "description": "Services supporting the Firefox browser and others"
}

mz_services = [
    {
        "name": "Firefox Accounts",
        "slug": "fxa",
        "description": "The Firefox Accounts Service",
        "url": "https://accounts.firefox.com",
        "category": "/api/v1/categories/1/",
    },
    {
        "name": "Firefox Hello",
        "slug": "fx-hello",
        "description": "The Firefox Hello Service",
        "url": "https://hello.firefox.com",
        "category": "/api/v1/categories/1/",
    },
    {
        "name": "Firefox Sync",
        "slug": "fx-sync",
        "description": "The Firefox Sync Service",
        "category": "/api/v1/categories/1/",
    },
    {
        "name": "Mozilla Location Service",
        "slug": "location",
        "description": "The Mozilla Location Service",
        "url": "https://location.services.mozilla.com",
        "category": "/api/v1/categories/1/",
    }
]

if __name__ == "__main__":
    api = Api(sys.argv[1], sys.argv[2])

    api.put('/api/v1/sites/1/', {
        "domain": "mozilla.org",
        "name": "Cloud Services Status Page"
    })
    api.post('/api/v1/categories/', mz)
    for svc in mz_services:
        api.post('/api/v1/services/', svc)
