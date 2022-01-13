#!/usr/bin/env python

__author__ = 'ferdous'

import os
import urllib2
import json
from utils import get_id_prefix


def process_file_and_get_concepts(folder_name, item):
    try:
        return [i.strip().split(' ')[1] for i in open(folder_name + '/' + item, 'r').readlines()]
    except IndexError as ie:
        print ie.message
    return []


def run(folder_name="data/concepts"):
    for item in os.listdir(folder_name):
        concept_name = item.split(' ')[1].split('.')[0]
        for i in open(folder_name + '/' + item):
            doc_id = get_id_prefix() + i.rstrip() + '.jpg'
            print doc_id
            print concept_name
            params = [{'id': doc_id, 'concepts': {'add': concept_name}}]
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
