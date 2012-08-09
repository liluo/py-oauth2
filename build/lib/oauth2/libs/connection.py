# -*- coding: utf-8 -*-
import urllib
from httplib2 import Http

class Connection(object):

    def __repr__(self):
        return '<OAuth2 Connection>'

    @classmethod
    def build_url(cls, url, path='', params={}):
        params = urllib.urlencode(params)
        params = '?%s'%params if params else ''
        url = path if path.startswith('http') else '%s%s'%(url, path)
        return '%s%s'%(url, params)

    @classmethod
    def run_request(cls, method, url, **opts):
        disable_ssl = opts.get('disable_ssl', True)
        http = Http(disable_ssl_certificate_validation=disable_ssl)
        headers = opts.pop('headers', {})
        body = None

        params = urllib.urlencode(opts)
        if method == 'POST':
            headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
            body = params
        elif params:
            url += '&%s'%url if '?' in url else '?%s'%params
        return http.request(url, method, body=body, headers=headers)
