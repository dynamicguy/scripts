# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log
from pprint import pprint
import urllib2
import base64
import time

username = 'admin'
password = 'password123'

# base64 encode the username and password
auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

class MethodRequest(urllib2.Request):
    def __init__(self, *args, **kwargs):
        if 'method' in kwargs:
            self._method = kwargs['method']
            del kwargs['method']
        else:
            self._method = None
        return urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self, *args, **kwargs):
        if self._method is not None:
            return self._method
        return urllib2.Request.get_method(self, *args, **kwargs)

def do_call_api(did, data):
    req = MethodRequest('http://localhost:8764/api/apollo/connectors/datasources/'+did, method='PUT')
    req.add_header('Authorization', "Basic %s" % auth)
    req.add_header('Content-type', 'application/json')
    req.add_header('Accept', 'application/json')
    req.add_data(data)
    return req
    

def run(file):
    with open(file) as data_file:
        data = json.loads(data_file.read())

        for item in data:
            did = item.get('id')
            cn = item.get('properties').get('collection')
            if('com' in did):
                if('skillshill' in cn):
                    req = do_call_api(did, json.dumps(item))
                    try:
                        pprint('put data for ' + did)
                        r = urllib2.urlopen(req)
                        pprint(r.read())
                    except urllib2.HTTPError as e:
                        print e.code
                        print e.read()
                        time.sleep(10)
                    finally:
                        time.sleep(1)


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file to scan for data sources")

    try:
        args = parser.parse_args()
        if args.file is None:
            args.file = 'all-dev-ds.json'
        log.ok('running... with options: %s ' % args)
        run(args.file)
    except:
        raise
        parser.print_help()
