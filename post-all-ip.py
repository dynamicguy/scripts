# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log
from pprint import pprint
import urllib
import http.client as httplib
import base64

username = 'admin'
password = 'zaq12345'

# base64 encode the username and password
# auth = base64.b64encode('%s:%s' % (username, password)).replace('\n', '')

def do_call_api(did, data):
    headers = {"Content-type": "application/json", "Accept": "application/json", "Authorization": "Basic YWRtaW46emFxMTIzNDU="}
    conn = httplib.HTTPConnection('118.67.215.231', 8764)
    conn.request("POST", "/api/apollo/index-pipelines/", data, headers)
    response = conn.getresponse()
    print(response.status, response.reason)

    result = response.read()
    pprint(result)
    conn.close()

def run(file):
    with open(file) as data_file:
        data = json.loads(data_file.read())

        for item in data:
            did = item.get('id')
            pprint('post data for: ' + did)
            do_call_api(did, json.dumps(item))


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file to scan for data sources")

    try:
        args = parser.parse_args()
        if args.file is None:
            args.file = 'all-prod-ip.json'
        log.ok('running... with options: %s ' % args)
        run(args.file)
    except:
        raise
        parser.print_help()
