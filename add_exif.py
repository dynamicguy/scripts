#!/usr/bin/env python
__author__ = 'ferdous'


import json
import urllib2
import os
import re
from utils import get_id_prefix


def slugify(inStr):
    removelist = ["a", "an", "as", "at", "before", "but", "by", "for", "from", "is", "in", "into", "like", "of", "off",
                  "on", "onto", "per", "since", "than", "the", "this", "that", "to", "up", "via", "with"]
    for a in removelist:
        aslug = re.sub(r'\b' + a + r'\b', '', inStr)
    aslug = re.sub('[^\w\s-]', '', aslug).strip().lower()
    aslug = re.sub('\s+', '-', aslug)
    return aslug


def process_file_and_get_exif(folder_name, item):
    try:
        lines = open(folder_name + '/' + item, 'r').readlines()
        keys = lines[0::2]
        values = lines[1::2]
        items = dict()
        for i, k in enumerate(keys):
            items['exif-' + slugify(k)[1:]] = values[i].strip()
        return items
    except IndexError as ie:
        print ie.message
    return []


def get_item_from_solr(doc_id):
    full_url = "http://localhost:8888/solr/images/select?facet=false&wt=python&hl=false&rows=1&fl=*&debugQuery=true&start=0&q={!s}{!s}&forceElevation=true&debug.explain.structured=true&req_type=doc&role=DEFAULT&role=api&qt=/lucid&user=admin&markExcludes=true".format(
        '{!raw+f=id}', doc_id)
    conn = urllib2.urlopen(full_url)
    return eval(conn.read())


def run(folder_name="data/exif"):
    for item in os.listdir(folder_name):
        img_file_name = item.split('.')[0] + '.jpg'
        doc_id = get_id_prefix() + img_file_name
        print doc_id
        solr_response = get_item_from_solr(doc_id)
        if solr_response.get('response').get('docs'):
            doc = solr_response.get('response').get('docs')[0]
        else:
            doc = dict()
        exif = process_file_and_get_exif(folder_name, item)
        print exif
        try:
            params = dict(doc.items() + exif.items())
            url = 'http://localhost:8888/solr/images/update/json'
            data = json.dumps([params])
            req = urllib2.Request(url)
            req.add_header('Content-type', 'application/json')
            req.data = data
            r = urllib2.urlopen(req)
            print r.read()
            r.close()
        except Exception, ex:
            pass



if __name__ == "__main__":
    run()
