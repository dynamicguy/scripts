#!/usr/bin/env python

__author__ = 'ferdous'

import sys
import json
import urllib2
import commands

def create_field(field_name):
    params = {
        "name": field_name,
        "default_value": "",
        "multi_valued": False,
        "stored": True,
        "indexed": True,
        "facet": False,
        "index_for_spellcheck": False,
        "synonym_expansion": False,
        "field_type": "text_en",
        "copy_fields": ["text_medium", "text_all"]
    }
    print params
    url = 'http://localhost:8888/api/collections/images/fields'
    data = json.dumps(params)
    req = urllib2.Request(url)
    req.add_header('Content-type', 'application/json')
    req.data = data
    r = urllib2.urlopen(req)
    print r.read()
    r.close()


def delete_field(field_name):
    command = 'curl -X DELETE http://localhost:8888/api/collections/images/fields/' + field_name
    print commands.getstatusoutput(command)


def run():
    items = ['orientation', 'focal-plane-y-resolution', 'metering-mode', 'date-and-time-original',
             'date-and-time-digitized', 'y-resolution', 'exposure-program', 'pixel-x-dimension', 'bits-per-sample',
             'focal-plane-x-resolution', 'compression', 'pixel-y-dimension', 'make', 'flash',
             'focal-plane-resolution-unit', 'image-length', 'aperture', 'shutter-speed', 'exposure-bias',
             'date-and-time', 'focal-length', 'has-xmp-block', 'photometric-interpretation', 'iso-speed',
             'planar-configuration', 'exposure', 'color-space', 'samples-per-pixel', 'xmp-date-and-time-original',
             'x-resolution', 'model', 'image-width', 'resolution-unit', 'software']

    for i in items:
        # delete_field('exif-' + i)
        create_field('exif-' + i)


if __name__ == "__main__":
    run()
