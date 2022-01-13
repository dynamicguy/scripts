# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log
from pprint import pprint
import httplib, urllib
import base64

username = 'ferdous'
password = 'please123'

# base64 encode the username and password
auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

def do_call_api(data):
    headers = {"Content-type": "application/json", "Accept": "application/json", "Authorization": "Basic %s" % auth}
    conn = httplib.HTTPConnection('localhost', 8764)
    print headers
    conn.request("POST", "/api/apollo/connectors/datasources", data, headers)
    response = conn.getresponse()
    print response.status, response.reason

    data = response.read()
    pprint(data)
    conn.close()

def run(file):
    with open(file) as data_file:
        data = json.loads(data_file.read())

    for item in data:
        did = item.get('id')
        cn = item.get('properties').get('collection')
        if('com' in did):
            if('bd' in cn):
                pprint('post data for ' + did + ' with collection as ' + cn)
          #pprint(item)


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file to scan for data sources")

    try:
        args = parser.parse_args()
        if args.file is None:
            args.file = './all-dev-ds.json'
        log.ok('running... with options: %s ' % args)
        run(args.file)
    except:
        raise
        parser.print_help()
