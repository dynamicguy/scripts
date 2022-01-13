#!/usr/bin/env python
import json

__author__ = 'ferdous'

import os
import urllib2
from utils import get_id_prefix
import xml.etree.ElementTree as ET


def run(folder_name="data/images"):
    for file_name in os.listdir(folder_name):
        solrId = get_id_prefix() + file_name
        xml_file = '/Users/ferdous/projects/digitalcandy/datam/data/solr_xml/' + file_name + '_solr.xml'
        print xml_file
        tree = ET.parse(xml_file)
        fields = tree.findall("field")
        params = [{'id': solrId, 'title': {'set': file_name}}]

        for field in fields:
            key = field.get('name')
            if key != 'id':
                params[0][key] = {'set': field.text}
        params[0]['id'] = solrId

        try:
            url = 'http://localhost:8888/solr/images/update/json'
            data = json.dumps(params)
            print data
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
