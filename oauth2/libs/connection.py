# -*- coding: utf-8 -*-
import urllib

class Connection(object):

    def __repr__(self):
        return '<OAuth2 Connection>'

    @classmethod
    def build_url(cls, url, path='', params={}):
        params = urllib.urlencode(params)
        params = '?%s'%params if params else ''
        url = path if path.startswith('http') else '%s%s'%(url, path)
        return '%s%s'%(url, params)
