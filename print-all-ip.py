# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json
import argparse
import log
from pprint import pprint
import urllib2
import base64
import time

username = 'admin'
password = 'password123'

# base64 encode the username and password
auth = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

class MethodRequest(urllib2.Request):
    def __init__(self, *args, **kwargs):
        if 'method' in kwargs:
            self._method = kwargs['method']
            del kwargs['method']
        else:
            self._method = None
        return urllib2.Request.__init__(self, *args, **kwargs)

    def get_method(self, *args, **kwargs):
        if self._method is not None:
            return self._method
        return urllib2.Request.get_method(self, *args, **kwargs)

def do_call_api(did, data):
    req = MethodRequest('http://localhost:8764/api/apollo/index-pipelines/'+did, method='PUT')
    req.add_header('Authorization', "Basic %s" % auth)
    req.add_header('Content-type', 'application/json')
    req.add_header('Accept', 'application/json')
    req.add_data(data)
    return req
    


def run(file):
    with open(file) as data_file:
        data = json.loads(data_file.read())
        fresh_data = []
        for item in data:
            did = item.get('id')
            if('_org' in did):
                pprint('print data for ' + did)
                item['stages'][0] = json.loads('{ "type" : "tika-parser", "id" : "tika_content_csv_disabled_stage", "includeImages" : true, "flattenCompound" : false, "addFailedDocs" : true, "addOriginalContent" : false, "contentField" : "_raw_content_", "contentEncoding" : "binary", "returnXml" : false, "keepOriginalStructure" : false, "extractHtmlLinks" : true, "extractOtherLinks" : false, "csvParsing" : false, "includeContentTypes" : [ ], "excludeContentTypes" : [ ], "type" : "tika-parser", "skip" : false, "label" : "tika-parser" }')
                item['stages'][3] = json.loads('{ "type" : "lang-detect", "id" : "conn_language_detection", "source" : [ "content", "title" ], "outputType" : "document", "outputKey" : "languages", "documentPostfix" : "_lang", "type" : "lang-detect", "skip" : false, "label" : "lang-detect" }')
                
                item['stages'][2] = json.loads('{ "type" : "field-mapping", "id" : "Dynamic_fields", "mappings" : [ { "source" : "Content-Encoding", "target" : "contentEncoding_s", "operation" : "move" }, { "source" : "Character-Set", "target" : "characterSet_s", "operation" : "move" }, { "source" : "Content-Length", "target" : "contentLength_l", "operation" : "move" }, { "source" : "FileSize", "target" : "fileSize_l", "operation" : "move" }, { "source" : "FileName", "target" : "fileName_s", "operation" : "move" }, { "source" : "Content-Type", "target" : "mimeType_s", "operation" : "move" }, { "source" : "MimeType", "target" : "mimeType_s", "operation" : "move" }, { "source" : "Title", "target" : "title", "operation" : "move" }, { "source" : "Description", "target" : "description", "operation" : "move" }, { "source" : "Subject", "target" : "subject", "operation" : "move" }, { "source" : "created", "target" : "dateCreated_dt", "operation" : "move" }, { "source" : "ContentCreated", "target" : "dateCreated_dt", "operation" : "move" }, { "source" : "meta:creation_date", "target" : "dateCreated_dt", "operation" : "move" }, { "source" : "Creation-Date", "target" : "dateCreated_dt", "operation" : "move" }, { "source" : "date", "target" : "dateCreated_dt", "operation" : "move" }, { "source" : "Author", "target" : "author", "operation" : "move" }, { "source" : "meta:author", "target" : "author", "operation" : "move" }, { "source" : "Contributor", "target" : "author", "operation" : "move" }, { "source" : "LastModifiedBy", "target" : "author", "operation" : "move" }, { "source" : "Last-Author", "target" : "author", "operation" : "move" }, { "source" : "fullname", "target" : "author", "operation" : "move" }, { "source" : "meta:last-author", "target" : "author", "operation" : "move" }, { "source" : "Last-Modified", "target" : "last_modified", "operation" : "move" }, { "source" : "fileLastModified", "target" : "last_modified", "operation" : "move" }, { "source" : "ContentLastModified", "target" : "last_modified", "operation" : "move" }, { "source" : "Last-Save-Date", "target" : "last_modified", "operation" : "move" }, { "source" : "fullText", "target" : "content_txt", "operation" : "move" }, { "source" : "plainTextContent", "target" : "content_txt", "operation" : "move" }, { "source" : "plainTextMessageContent", "target" : "content_txt", "operation" : "move" }, { "source" : "body", "target" : "content_txt", "operation" : "move" }, { "source" : "content", "target" : "content_txt", "operation" : "move" }, { "source" : "keyword", "target" : "keywords", "operation" : "move" }, { "source" : "Keywords", "target" : "keywords", "operation" : "move" }, { "source" : "messageSubject", "target" : "title", "operation" : "move" }, { "source" : "name", "target" : "title", "operation" : "move" }, { "source" : "Page-Count", "target" : "pageCount_i", "operation" : "move" }, { "source" : "PageCount", "target" : "pageCount_i", "operation" : "move" }, { "source" : "Slide-Count", "target" : "pageCount_i", "operation" : "move" }, { "source" : "Slides", "target" : "pageCount_i", "operation" : "move" }, { "source" : "xmpTPg:NPages", "target" : "pageCount_i", "operation" : "move" }, { "source" : "parsing_time", "target" : "parsing_time_l", "operation" : "move" }, { "source" : "parsing", "target" : "parsing_s", "operation" : "move" }, { "source" : "Comments", "target" : "comments", "operation" : "move" }, { "source" : "resourceName", "target" : "resourcename_s", "operation" : "move" }, { "source" : "resource_name", "target" : "resourcename_s", "operation" : "move" }, { "source" : "Content-Location", "target" : "url", "operation" : "move" }, { "source" : "meta:character-count", "target" : "character-count_i", "operation" : "move" }, { "source" : "Word-Count", "target" : "wordCount_i", "operation" : "move" }, { "source" : "type", "target" : "type_s", "operation" : "move" }, { "source" : "X-Parsed-By", "target" : "xParsedBy_ss", "operation" : "move" }, { "source" : "body.links.anchor", "target" : "body_links_anchor_ss", "operation" : "move" }, { "source" : "body.links.params.alt", "target" : "body_links_params_alt_ss", "operation" : "move" }, { "source" : "body.links.params.type", "target" : "body_links_params_type_ss", "operation" : "move" }, { "source" : "body.links.title", "target" : "body_links_title_ss", "operation" : "move" }, { "source" : "body.links.targetUri", "target" : "body_links_targetUri_ss", "operation" : "move" }, { "source" : "/(.*)_[isltbfd]s?/", "operation" : "keep" }, { "source" : "/(.*)_txt/", "operation" : "keep" }, { "source" : "/(.*)_en/", "operation" : "keep" }, { "source" : "/(.*)_dts?/", "operation" : "keep" }, { "source" : "/(.*)_t[ilfd]/", "operation" : "keep" }, { "source" : "/(.*)_p/", "operation" : "keep" }, { "source" : "/(.*)_c/", "operation" : "keep" }, { "source" : "/(.*)_coordinate/", "operation" : "keep" }, { "source" : "/attr_(.*)/", "operation" : "keep" }, { "source" : "/random_(.*)/", "operation" : "keep" }, { "source" : "/ignored_(.*)/", "operation" : "keep" } ], "reservedFieldsMappingAllowed" : false, "type" : "field-mapping", "skip" : false, "label" : "field-mapping" }')
            
                item['stages'].append(json.loads('{ "type" : "solr-index", "id" : "solr-default", "enforceSchema" : true, "dateFormats" : [ ], "params" : [ ], "bufferDocsForSolr" : false, "unmapped" : { "source" : "/(^.*)$/", "target" : "$1_txt", "operation" : "move" }, "type" : "solr-index", "skip" : false, "label" : "solr-index" }'))
                item['stages'][4] = json.loads('{ "type": "lookup-extractor", "id": "lookup-extractor-default", "rules": [ { "source": [ "description" ], "target": "color", "entityTypes": [ { "name": "Color", "entityDefinitions": [ "colours.lst" ] } ], "additionalEntities": [], "caseSensitive": false }, { "source": [ "description" ], "target": "city", "entityTypes": [ { "name": "City", "entityDefinitions": [ "city.lst" ] } ], "additionalEntities": [], "caseSensitive": false } ], "type": "lookup-extractor", "skip": false, "label": "lookup-extractor" }')
                # pprint(item['stages'])
                for st in item['stages']:
                    pprint(st.get('type'))
                fresh_data.append(item)
                print fresh_data
                    
        # out_file = open('fresh-ips.json', 'w')
        # pprint('writing data in file')
        # out_file.write(json.dumps(fresh_data, sort_keys=False, indent=2))
        # out_file.close()
                    
                # req = do_call_api(did, json.dumps(item))
                # try:
                #     pprint('put data for ' + did)
                #     r = urllib2.urlopen(req)
                #     pprint(r.read())
                # except urllib2.HTTPError as e:
                #     print e.code
                #     print e.read()
                #     time.sleep(4)
                # finally:
                #     time.sleep(1)
                
            

if __name__ == "__main__" :
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file to scan for data sources")

    try:
        args = parser.parse_args()
        if args.file is None:
            args.file = 'all-dev-ip.json'
        log.ok('running... with options: %s ' % args)
        run(args.file)
    except:
        raise
        parser.print_help()
