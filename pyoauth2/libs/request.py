# -*- coding: utf-8 -*-
import requests

from .response import Response


class Request(object):

    def __init__(self, method, uri, **opts):
        self.method = method
        self.uri = uri
        self.headers = opts.pop('headers', {})
        self.body = opts.pop('body', None)
        self.parse = opts.pop('parse', 'json')
        self.files = opts.pop('files', {})
        self.opts = opts

    def __repr__(self):
        return '<OAuth2 Request>'

    def request(self):
        if self.method in ('POST', 'PUT'):
            response = requests.request(self.method, self.uri, data=self.opts, files=self.files, headers=self.headers)
        else:
            response = requests.request(self.method, self.uri, params=self.opts, headers=self.headers)

        response = Response(response, parse=self.parse)

        status = response.status_code
        #TODO raise error
        if status in (301, 302, 303, 307):
            return response
        elif 200 <= status < 400:
            return response
        elif 400 <= status < 500:
            return response
        elif 500 <= status < 600:
            return response
        return response
