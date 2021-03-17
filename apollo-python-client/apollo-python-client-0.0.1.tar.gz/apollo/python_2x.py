#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import urllib2
from urllib import urlencode


def http_request(url, timeout, headers={}):
    try:
        request = urllib2.Request(url, headers=headers)
        res = urllib2.urlopen(request, timeout=timeout)
        body = res.read().decode("utf-8")
        return res.code, body
    except urllib2.HTTPError as e:
        if e.code == 304:
            logging.getLogger(__name__).warning("http_request error,code is 304, maybe you should check secret")
            return 304, None
        logging.getLogger(__name__).warning("http_request error,code is %d, msg is %s", e.code, e.msg)
        raise e


def url_encode(params):
    return urlencode(params)
