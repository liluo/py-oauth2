# -*- coding: utf-8 -*-
import urlparse
import json

def to_json(txt):
    try:
        return json.loads(txt)
    except ValueError:
        return txt

def to_query(txt):
    qs = urlparse.parse_qsl(txt)
    ret = dict(qs)
    return _check_expires_in(ret)

def to_text(txt):
    return txt

def _check_expires_in(ret):
    expires_in = ret.get('expires_in')
    if expires_in and expires_in.isdigit():
        ret['expires_in'] = int(expires_in)
    return ret

PARSERS = {
        'text': to_text,
        'json': to_json,
        'query': to_query,
        }


CONTENT_TYPES = {
            'text/plain': 'text',
            'text/javascript': 'json',
            'application/json': 'json',
            'application/x-www-form-urlencoded': 'query',
            }

class Response(object):

    def __init__(self, response, **opts):
        response, body = response
        self.body = body
        self.response = response
        self.reason = response.reason
        self.status = response.status
        self.content_type = response.get('content-type')

        options = { 'parse': 'text' }
        options.update(opts)

        self.options = options

    def __repr__(self):
        return '<OAuth2 Response>'

    @property
    def parsed(self):
        format = self.options['parse']
        func = PARSERS.get(format, to_text)
        return func(self.body)
