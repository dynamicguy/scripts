# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log
import os
from pprint import pprint
import httplib, urllib
import base64

username = 'ferdous'
password = 'please123'

# base64 encode the username and password
auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

def do_call_api(qid, data):
    headers = {"Content-type": "application/json", "Accept": "application/json", "Authorization": "Basic %s" % auth}
    conn = httplib.HTTPConnection('localhost', 8764)
    conn.request("PUT", "/api/apollo/query-pipelines/" + qid, data, headers)
    response = conn.getresponse()
    print response.status, response.reason

    result = response.read()
    pprint(result)
    conn.close()

def run(file):
    for f in os.listdir(file):
		if(f.endswith('bin')):
			u = '/api/apollo/blobs/' + f
			s = '@blobs/' + f
			print 'curl -u admin:password123 -X PUT --data-binary ' + s + ' -H "Content-type: application/octet-stream" http://localhost:8764' + u


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file to scan for data sources")

    try:
        args = parser.parse_args()
        if args.file is None:
            args.file = 'blobs'
        #log.ok('running... with options: %s ' % args)
        run(args.file)
    except:
        raise
        parser.print_help()
