# -*- coding: utf-8 -*-
import urllib
from io import BytesIO
from StringIO import StringIO
from httplib2 import Http

from .response import Response
from .multipart import build_multipart

class Request(object):

    def __init__(self, method, uri, **opts):
        self.method = method
        self.uri = uri
        self.headers = opts.pop('headers', {})
        self.body = opts.pop('body', None)

        self.disable_ssl = opts.pop('disable_ssl', True)
        self.http = Http(disable_ssl_certificate_validation=self.disable_ssl)
        self.content_type = 'application/x-www-form-urlencoded'
        self.opts = opts

    def __repr__(self):
        return '<OAuth2 Request>'

    def request(self):
        parse = self.opts.pop('parse', 'json')
        files = self.opts.pop('files', {})
        params = urllib.urlencode(params_u2utf8(self.opts))

        if self.method in ('POST', 'PUT'):
            (body, content_type) = self.__encode_files(files, self.opts) if files else (params, self.content_type)
            self.headers.update({'Content-Type': content_type})
            self.body = body

        elif self.opts:
            self.uri += '&%s'%params if '?' in self.uri else '?%s'%params

        response = self.send()
        response = Response(response, parse=parse)

        status = response.status
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

    def send(self):
        return self.http.request(self.uri, self.method, body=self.body, headers=self.headers)

    def __encode_files(self, files, params):
        if not files or isinstance(files, str):
            return None

        fields = []
        for k, v in tuples(files):
            if isinstance(v, (tuple, list)):
                fn, fp = v
            else:
                fn = guess_filename(v) or k
                fp = v
            if isinstance(fp, str):
                fp = StringIO(fp)
            if isinstance(fp, bytes):
                fp = BytesIO(fp)

            fields.append((k, (fn, fp.read())))

        for k, vs in tuples(params):
            if isinstance(vs, list):
                for v in vs:
                    fields.append((k, str(v)))
            else:
                fields.append((k, str(vs)))

        body, content_type = build_multipart(fields)

        return body, content_type


def guess_filename(obj):
    name = getattr(obj, 'name', '')
    if all([name, not name.startswith('<'), not name.endswith('>')]):
        return name

def tuples(obj):
    if isinstance(obj, dict):
        return list(obj.items())
    elif hasattr(obj, '__iter__'):
        try:
            dict(obj)
        except ValueError:
            pass
        else:
            return obj
    raise ValueError('not a dict or a list of 2-tuples required')

def params_u2utf8(params):
    u2utf8 = lambda obj: isinstance(obj, unicode) and obj.encode('utf-8') or obj
    return dict([(k, u2utf8(v)) for k, v in params.items()])
