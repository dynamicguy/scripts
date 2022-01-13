# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log
from pprint import pprint
import urllib
import base64
import http.client as httplib

username = 'admin'
password = 'password123'

# base64 encode the username and password
# auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

def do_call_api(qid, data):
    headers = {"Content-type": "application/json", "Accept": "application/json", "Authorization": "Basic YWRtaW46emFxMTIzNDU="}
    conn = httplib.HTTPConnection('118.67.215.231', 8764)
    conn.request("PUT", "/api/apollo/query-pipelines/" + qid, data, headers)
    response = conn.getresponse()

    result = response.read()
    pprint(result)
    conn.close()

def run(file):
    with open(file) as data_file:
        data = json.loads(data_file.read())

    for item in data:
        did = item.get('id')
        pprint('post data for ' + did)
        do_call_api(did, json.dumps(item))


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file to scan for data sources")

    try:
        args = parser.parse_args()
        if args.file is None:
            args.file = 'all-dev-qp.json'
        log.ok('running... with options: %s ' % args)
        run(args.file)
    except:
        raise
        parser.print_help()
