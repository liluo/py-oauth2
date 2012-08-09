# -*- coding: utf-8 -*-

class Request(object):

    def __init__(self, method, url, opts={}):
        self.method = method
        self.url = url
        self.headers = opts.get('headers', {})
        self.body = opts.get('body', '')

    def __repr__(self):
        return '<OAuth2 Request>'
