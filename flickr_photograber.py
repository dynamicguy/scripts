#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson as json
from time import sleep
import urllib2
import poster.encode
import poster.streaminghttp
from utils import get_id_prefix, get_id_prefix_src


opener = poster.streaminghttp.register_openers()


def run():
    url = 'http://api.flickr.com/services/feeds/photos_public.gne?format=json'
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    jsonp = f.read()
    try:
        rs = jsonp[jsonp.index('(') + 1: jsonp.rindex(')')]
        jsn = json.loads(rs)
        items = jsn.get('items')
        for item in items:
            img_url = item.get('media').get('m')
            download(img_url, item)
            sleep(1)
    except Exception, ex:
        print ex
        # print jsonp


def update_attributes(file_name, item):
    solrId = get_id_prefix() + file_name
    params = [
        {
            'id': solrId,
            'body': {'set': item.get('description')},
            'title': {'set': item.get('title')},
            'author': {'set': item.get('author').strip()},
            'keywords': {'set': item.get('tags')},
            'url': {'set': item.get('link').strip()},
            'date_taken': {'set': item.get('date_taken').strip()},
            'fileName': {'set': file_name}
        }
    ]
    url = 'http://localhost:8888/solr/images/update/json'
    data = json.dumps(params)
    req = urllib2.Request(url)
    req.add_header('Content-type', 'application/json')
    req.data = data
    r = urllib2.urlopen(req)
    print r.read()


def index(file_name, item):
    upload_file_url = "http://localhost:8888/solr/images/update/extract?literal.id=" + file_name
    params = {
        'filename': open(get_id_prefix_src() + file_name, 'rb'),
        'description': item.get('description')
    }
    datagen, headers = poster.encode.multipart_encode(params)
    response = opener.open(urllib2.Request(upload_file_url, datagen, headers))
    rsp = response.read()
    sleep(1)
    update_attributes(file_name, item)


def download(img_url, item):
    print 'downloading with urllib2', img_url
    file_name = img_url.split('/')[-1]
    imf = urllib2.urlopen(img_url)
    data = imf.read()
    with open(get_id_prefix_src() + file_name, 'wb') as code:
        code.write(data)
        sleep(1)
        index(file_name, item)


if __name__ == '__main__':
    run()






# {
#   "username": "ferdous",
#   "password": "6050ce63e4bce6764cb34cac51fb44d1",
#   "apiKey": "special-key"
# }

