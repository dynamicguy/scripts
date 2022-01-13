#!/usr/bin/env python

__author__ = 'ferdous'

import os
import urllib2

import poster.encode
import poster.streaminghttp


def run(folder_name="images"):
    opener = poster.streaminghttp.register_openers()
    for item in os.listdir(folder_name):
        file_name = item.split('.')[0]
        upload_file_url = "http://localhost:8888/solr/images/update/extract?literal.id=" + file_name + "&commit=true"
        params = {'filename': open(folder_name + '/' + item, 'rb'), 'description': item}
        datagen, headers = poster.encode.multipart_encode(params)
        response = opener.open(urllib2.Request(upload_file_url, datagen, headers))
        print response.read()


if __name__ == "__main__":
    run()
