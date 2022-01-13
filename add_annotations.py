#!/usr/bin/env python

__author__ = 'ferdous'

import os
import urllib2
import json
from utils import get_id_prefix

def process_file_and_get_annotations(folder_name, item):
    try:
        return [i.strip().split(' ')[1] for i in open(folder_name + '/' + item, 'r')]
    except IndexError as ie:
        print ie.message
    return []


def run(folder_name="data/annotations"):
    for item in os.listdir(folder_name):
        file_name = item.split('.')[0] + '.jpg'
        doc_id = get_id_prefix() + file_name
        print doc_id
        annotations = process_file_and_get_annotations(folder_name, item)
        params = [{'id': doc_id, 'annotations': {'set': annotations}}]
        url = 'http://localhost:8888/solr/images/update/json'
        data = json.dumps(params)
        req = urllib2.Request(url)
        req.add_header('Content-type', 'application/json')
        req.data = data
        r = urllib2.urlopen(req)
        print r.read()
        r.close()


if __name__ == "__main__":
    run()
