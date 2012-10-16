# -*- coding: utf-8 -*-
import time
import urlparse

class AccessToken(object):

    def __init__(self, client, token, **opts):
        self.client = client
        self.token = token
   
        [setattr(self, attr, opts.pop(attr)) for attr in ['refresh_token', 'expires_in', 'expires_at'] if opts.has_key(attr)]

        if hasattr(self, 'expires_in') and str(self.expires_in).isdigit():
            self.expires_at = int(time.time()) + int(self.expires_in)

        self.opts = { 'mode': opts.pop('mode', 'header'),
                      'header_format': opts.pop('header_format', 'Bearer %s'),
                      'param_name': opts.pop('param_name', 'bearer_token'),
                    }
        self.params = opts

    def __repr__(self):
        return '<OAuth2 AccessToken>'

    @classmethod
    def from_hash(cls, client, **opts):
        return cls(client, opts.pop('access_token', ''), **opts)

    @classmethod
    def from_kvform(cls, client, kvform):
        opts = dict(urlparse.parse_qsl(kvform))
        return cls(client, opts.pop('access_token', ''), **opts)

    def refresh(self, **opts):
        if not getattr(self, 'refresh_token', None):
            raise 'A refresh_token is not available'

        opts = { 'client_id': self.client.id,
                 'client_secret': self.client.secret,
                 'refresh_token': self.refresh_token,
                 'grant_type': 'refresh_token',
               }
        new_token = self.client.get_token(**opts)
        return new_token

    def request(self, method, url, **opts):
        opts = self.__set_token(**opts)
        return self.client.request(method, url, **opts)

    def get(self, url, **opts):
        return self.request('GET', url, **opts)

    def post(self, url, **opts):
        return self.request('POST', url, **opts)

    def put(self, url, **opts):
        return self.request('PUT', url, **opts)

    def patch(self, url, **opts):
        return self.request('PATCH', url, **opts)

    def delete(self, url, **opts):
        return self.request('DELETE', url, **opts)

    @property
    def headers(self):
        return {'Authorization': self.opts['header_format'] % self.token}

    def __set_token(self, **opts):
        mode = self.opts['mode']
        if mode == 'header':
            headers = opts.get('headers', {})
            headers.update(self.headers)
            opts['headers'] = headers
        elif mode == 'query':
            params = opts.get('params', {})
            params[self.opts['param_name']] = self.token
            opts['params'] = params
        elif mode == 'body':
            body = opts.get('body', {})
            if isinstance(body, dict):
                opts['body'][self.opts['param_name']] = token
            else:
                opts['body'] += "&%s=%s"%(self.opts['param_name'], self.token)
        else:
            raise "invalid :mode option of %s"%(self.opts['param_name'])

        return opts
