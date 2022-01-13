# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log
from pprint import pprint
import urllib
import base64
import time
import http.client, urllib.parse

username = 'admin'
password = 'password123'

# base64 encode the username and password
# auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')



def do_call_api(did, data):
    # url = 'http://118.67.215.231:8764/api/apollo/index-pipelines/'+did    
    # params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/json",
            "Accept": "application/json",
            'Authorization': "Basic YWRtaW46emFxMTIzNDU="}
    conn = http.client.HTTPConnection('118.67.215.231', 8764)
    conn.request("PUT", '/api/apollo/index-pipelines/'+did, data, headers)
    response = conn.getresponse()
    print(response.status, response.reason)

    res = response.read()
    conn.close()
    return res

    # req.add_header('Authorization', "Basic YWRtaW46emFxMTIzNDU=")
    # req.add_header('Content-type', 'application/json')
    # req.add_header('Accept', 'application/json')
    # req.add_data(data)
    # return req
    

def run(file):
    with open(file) as data_file:
        data = json.loads(data_file.read())

        for item in data:
            did = item.get('id')
            # if('_com' in did):
            req = do_call_api(did, json.dumps(item))
            print(req)
                # try:
                #     pprint('put data for ' + did)
                #     r = urllib.request.urlopen(req)
                #     pprint(r.read())
                # except Exception as e:
                #     time.sleep(10)
                # finally:
                #     time.sleep(1)
                


if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file to scan for data sources")

    try:
        args = parser.parse_args()
        if args.file is None:
            args.file = 'all-dev-ip.json'
        log.ok('running... with options: %s ' % args)
        run(args.file)
    except:
        raise
        parser.print_help()
