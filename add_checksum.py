#!/usr/bin/env python
import json

__author__ = 'ferdous'

import os
import urllib2
from utils import get_id_prefix, get_id_prefix_src

import hashlib


def md5_for_file(f, block_size=2 ** 20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()


def hashfile(afile, hasher, blocksize=65536):
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    return hasher.hexdigest()


def index_data(params):
    url = 'http://localhost:8888/solr/images/update/json'
    data = json.dumps(params)
    req = urllib2.Request(url)
    req.add_header('Content-type', 'application/json')
    req.data = data
    r = urllib2.urlopen(req)
    rsp = r.read()
    r.close()
    return rsp


def run(folder_name="data/thumbnails"):
    for file_name in os.listdir(folder_name):
        solrId = get_id_prefix() + file_name
        fname = get_id_prefix_src() + file_name
        checksum = hashfile(open(fname, 'rb'), hashlib.sha256())
        print checksum
        params = [{'id': solrId, 'checksum': {'set': checksum}}]
        print index_data(params)


if __name__ == "__main__":
    run()
