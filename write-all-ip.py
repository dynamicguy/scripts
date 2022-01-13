# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log
from pprint import pprint
import httplib, urllib


def run(file):
    with open(file) as data_file:
        data = json.loads(data_file.read())
        for item in data:
            did = item.get('id')
            out_file = open('pipelines/index/'+did+'.json', 'w')
            pprint('writing data in file ' + 'pipelines/index/'+did+'.json')
            out_file.write(json.dumps(item, sort_keys=False, indent=2))
            out_file.close()


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
