# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log

def run(file):
    for item in open(file):
        try:
            print item
        except:
            pass

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file to scan for data sources")

    try:
        args = parser.parse_args()
        log.ok('running... with options: %s ' % args)
        run(args.file)
    except:
        parser.print_help()
