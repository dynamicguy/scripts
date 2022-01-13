# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log
from pprint import pprint
import httplib, urllib
import base64

username = 'admin'
password = 'password123'

# base64 encode the username and password
auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

def do_call_api(did, data):
    headers = {"Content-type": "application/json", "Accept": "application/json", "Authorization": "Basic %s" % auth}
    conn = httplib.HTTPConnection('localhost', 8764)
    conn.request("DELETE", "/api/apollo/connectors/datasources/" + did, data, headers)
    response = conn.getresponse()
    print response.status

    result = response.read()
    conn.close()

def run(file):
    with open(file) as data_file:
        data = json.loads(data_file.read())

    for item in data:
        did = item.get('id')
        if('com' in did):
            pprint('put data for ' + did)
            do_call_api(did, None)


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file to scan for data sources")

    try:
        args = parser.parse_args()
        if args.file is None:
            args.file = 'all-prod-ds.json'
        log.ok('running... with options: %s ' % args)
        run(args.file)
    except:
        raise
        parser.print_help()
