__author__ = 'ferdous'

import os
import sys
import json
import httplib2

HTTP_CLIENT = httplib2.Http()

##
def get_env(key, default=None):
    if key in os.environ:
        return os.environ[key]
    return default

##
def is_mac():
    return (sys.platform == "darwin")


def get_id_prefix_src():
    if is_mac():
        return '/Users/ferdous/projects/digitalcandy/datam/data/thumbnails/'
    else:
        return '/data/medialab.liacs.nl/mirflickr/mirflickr25k/images/'


def get_id_prefix():
    if is_mac():
        return 'file:/Users/ferdous/projects/digitalcandy/datam/data/thumbnails/'
    else:
        return 'file:/data/medialab.liacs.nl/mirflickr/mirflickr25k/images/'


##
def parse_opts(args):
    data = {}
    for arg in args:
        key, val = arg.split('=', 1)

        # make a list out of any key specified more then once
        if key in data:
            oldval = data[key]
            if type(oldval) is list:
                oldval.append(val)
            else:
                data[key] = [oldval, val]
        else:
            data[key] = val
    return data


##
def json_http(url, method='GET', data=None):
    body = None;
    if (data): body = json.dumps(data)
    resp, content = HTTP_CLIENT.request(
        url, method=method, body=body,
        headers={'Content-Type': 'application/json'})

    # fail if not status 2xx
    if 0 != str(resp.status).find('2'):
        err = content
        try:
            err = pretty_json(json.loads(content))
        except:
            # IGNORE, use the raw error instead
            pass
        raise Exception(method + ' ' + url + ' => ' + str(resp.status) + "\n" + err)

    if 204 == resp.status: return None
    return json.loads(content)

##
def pretty_json(data, indent=''):
    pretty = json.dumps(data, indent=2)
    return pretty.replace("\n", "\n" + indent)

##

COLLECTION = get_env('LWE_COLLECTION', 'images')
LWE_URL = get_env('LWE_URL', 'http://localhost:8888')
SOLR_URL = get_env('LWE_SOLR_URL', LWE_URL + '/solr/' + COLLECTION + '/update/json')
UI_URL = get_env('LWE_UI_URL', 'http://localhost:8989')
