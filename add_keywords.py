#!/usr/bin/env python
import json

__author__ = 'ferdous'

import os
import urllib2
from utils import get_id_prefix


def run(folder_name="data/tags"):
    for file_name in os.listdir(folder_name):
        solrId = get_id_prefix() + file_name.split('.')[0] + '.jpg'
        tag_file = 'data/tags/' + file_name
        tags = open(tag_file, 'r').readlines()
        cleaned_tags = [item.strip() for item in tags]
        params = [{'id': solrId, 'keywords': {'set': cleaned_tags}}]
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
