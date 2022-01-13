# -*- coding: utf-8 -*-
# !/usr/bin/env python
import argparse
import json
import re
from bs4 import BeautifulSoup
import mysql.connector
import requests
import unidecode

import log

token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJMbXVyX3M5N1BPS2k2ODZzTmZTTVFPamdJYjRqdVFEQm0zREVBZk15YzBjIn0.eyJqdGkiOiI1ZDg1OGFlZi01OWI0LTQ2ZjktYWYzYS01ZDNmMjNiZGY2MTkiLCJleHAiOjE1ODA2MDc0NjMsIm5iZiI6MCwiaWF0IjoxNTgwNTczNDIxLCJpc3MiOiJodHRwczovL3Nzby50aGVkYWlseXN0YXIubmV0L2F1dGgvcmVhbG1zL2poaXBzdGVyIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjQ2MDAxYWJkLTMxYjktNDc3MS1hMDM3LWExNGNlMDZmNTM4OSIsInR5cCI6IkJlYXJlciIsImF6cCI6IndlYl9hcHAiLCJhdXRoX3RpbWUiOjE1ODA1NzE0NjMsInNlc3Npb25fc3RhdGUiOiI4NjBlZjMwOC0wNTczLTRjZWYtOWYzNS05MDA4YTliOWIyM2YiLCJhY3IiOiIwIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIlJPTEVfVVNFUiIsIm9mZmxpbmVfYWNjZXNzIiwiUk9MRV9BRE1JTiIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgamhpcHN0ZXIgbWljcm9wcm9maWxlLWp3dCBlbWFpbCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGFkZHJlc3MgcGhvbmUiLCJ1cG4iOiJmZXJkb3VzIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImFkZHJlc3MiOnt9LCJyb2xlcyI6WyJST0xFX1VTRVIiLCJvZmZsaW5lX2FjY2VzcyIsIlJPTEVfQURNSU4iLCJ1bWFfYXV0aG9yaXphdGlvbiJdLCJuYW1lIjoiTnVydWwgRmVyZG91cyIsImdyb3VwcyI6WyJST0xFX1VTRVIiLCJvZmZsaW5lX2FjY2VzcyIsIlJPTEVfQURNSU4iLCJ1bWFfYXV0aG9yaXphdGlvbiJdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmZXJkb3VzIiwiZ2l2ZW5fbmFtZSI6Ik51cnVsIiwiZmFtaWx5X25hbWUiOiJGZXJkb3VzIiwiZW1haWwiOiJudXJ1bEBmZXJkby51cyJ9.cr5N9zEXLfFrb3rsX5obSdYWZqq45ydYmII8hcQ-LZjwxFPhDyZNRf5gsrKErUR4gYG1N0-qDaimXbKw4SrtpwHMJsMptaQa3xTKJMz1R_Fm0OIiMarlostwYeVfTkN4KMrBPW1ZsWNEkmTw8YWr1q7LOZ-EG8r8eZv6Wm87s6fycpNs4g9wLOqaoWbGFf2lk09tlCjiwPYLUy__EmRhY_bjOYmUoPj5zAxefhCNdXe0G2Vy9susUIzGResZIyfTpmCvY9VfS6jmLYEcNyYsOMUft6SOU04fpMcNk9C2RG9YhoXoyOQf6Hz3X1a1ynJkppyfZ1Keh_dxWSt1BrAiZg'

config = {
    'user': 'ferdous',
    'password': 'f',
    'host': '127.0.0.1',
    'database': 'tds_bangla'
}


def slugify(text):
    text = unidecode.unidecode(text).lower()
    return re.sub(r'[\W_]+', '-', text)

def upload_img(img_url, nid):
    myfile = requests.get(img_url)

    if myfile.status_code == 200:
        ipath = '/tmp/' + str(nid) + '.jpg'
        img = open(ipath, 'wb').write(myfile.content)

        upload_url = 'https://img.thedailystar.net/upload'

        upload_headers = {
            'Accept': '*/*',
            'Host': 'img.thedailystar.net'
        }

        upload_data = {'userfille': open(ipath)}

        response = requests.request('POST', upload_url, headers=upload_headers, files=upload_data)
        result = response.text.encode('utf8')
        parsed_html = BeautifulSoup(result, features="html.parser")
        hash = parsed_html.body.find('h1').text
        return hash

def create_news(payload):
    url = "https://privatebeta.thedailystar.net/api/news"
    data = json.dumps(payload)

    headers = {
        'Accept': 'text/json',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token
    }

    response = requests.request("POST", url, headers=headers, data=data)
    return response

def create_category(payload):
    url = "https://privatebeta.thedailystar.net/api/categories"
    data = json.dumps(payload)

    headers = {
        'Accept': 'text/json',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token
    }

    response = requests.request("POST", url, headers=headers, data=data)

    return response

def process_row(row):
    (nid, title, body, intro, byline, short_headline, caption, color, contact_no, date, designation, email,
     external_link, file_image_alt_text, file_image_title_text, lead_news_behavior, news_body, publish_date,
     section_title, shoulder, sub_headline, featured_image_fid, uri, filename, author_target_id, author_bio_value) = row

    print('processing row with nid ', nid)
    fullImageUrl = "https://assetsds.cdnedge.bluemix.net/bangla/sites/default/files/" + uri.replace("public://", "")

    news_slug = slugify(title) + '-' + str(nid)
    news_slug = news_slug.lstrip('-')

    payload = {
        "id": nid,
        "title": title,
        "slug": news_slug,
        "headline": title,
        "featuredImage": str(fullImageUrl),
        "imageCaption": filename,
        "highlight": title,
        "subHead": sub_headline,
        "shoulder": shoulder,
        "intro": intro,
        "content": body,
        "newsType": u"WEB",
        "newsLayout": u"DEFAULT",
        "byline": byline,
        "liveEmbeddedCode": None,
        "publishDate": publish_date.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),  # "2020-01-30T08:50:10.153014Z"
        "hideAds": False,
        "commentable": False,
        "viewCount": 1,
        "language": u"BN",
        "status": u"PUBLISHED",
        "authorId": 1,
        "authorName": u"Staff Reporter",
        "relatedId": None,
        "relatedTitle": None,
        "magazineId": None,
        "magazineTitle": None,
        "locationId": None,
        "locationStreetAddress": None,
        "tags": [],
        "categories": [],
        "newsOptions": []
    }
    return payload


def search_categories(query):
    url = "https://privatebeta.thedailystar.net/api/_search/categories?page=0&query=%s&size=2&sort=id,desc" % query
    print(url)

    payload = {}
    headers = {
        'Accept': 'text/json',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def search_news(query):
    url = "https://privatebeta.thedailystar.net/api/_search/news?page=0&query=%s&size=2&sort=id,desc" % query
    print(url)

    payload = {}
    headers = {
        'Accept': 'text/json',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def run(start, offset):
    log.ok('starting... with options: %s,%s ' % (start, offset))
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()
    catCursor = cnx.cursor()

    query = (
        "SELECT n.nid, n.title, r.body_value, fdfi.field_intro_value, fdfb.field_byline_value, fdfsl.field_short_headline_value, fdfc.field_caption_value, fdfco.field_color_value, fdfcn.field_contact_no_value, fdfd.field_date_value, fdfdn.field_designation_value, fdfe.field_email_value, fdfel.field_external_link_value, fdffiat.field_file_image_alt_text_value, fdffitt.field_file_image_title_text_value, fdflnb.field_lead_news_behavior_value, fdfnb.field_news_body_value, fdfpd.field_publish_date_value, fdfst.field_section_title_value, fdfs.field_shoulder_value, fdfsh.field_sub_headline_value, fdffi.field_featured_image_fid, fm.uri, fm.filename, fdfa.field_author_target_id, fdfab.field_author_bio_value FROM node n LEFT JOIN field_data_body r ON n.nid = r.entity_id AND n.vid = r.revision_id LEFT JOIN field_data_field_intro fdfi ON n.nid = fdfi.entity_id AND n.vid = fdfi.revision_id LEFT JOIN field_data_field_byline fdfb ON n.nid = fdfb.entity_id AND n.vid = fdfb.revision_id LEFT JOIN field_data_field_short_headline fdfsl ON n.nid = fdfsl.entity_id AND n.vid = fdfsl.revision_id LEFT JOIN field_data_field_featured_image fdffi ON n.nid = fdffi.entity_id AND n.vid = fdffi.revision_id LEFT JOIN field_data_field_author fdfa ON n.nid = fdfa.entity_id AND n.vid = fdfa.revision_id LEFT JOIN field_data_field_author_bio fdfab ON n.nid = fdfab.entity_id AND n.vid = fdfab.revision_id LEFT JOIN file_managed fm ON fdffi.field_featured_image_fid = fm.fid LEFT JOIN field_data_field_caption fdfc ON n.nid = fdfc.entity_id AND n.vid = fdfc.revision_id LEFT JOIN field_data_field_color fdfco ON n.nid = fdfco.entity_id AND n.vid = fdfco.revision_id LEFT JOIN field_data_field_contact_no fdfcn ON n.nid = fdfcn.entity_id AND n.vid = fdfcn.revision_id LEFT JOIN field_data_field_date fdfd ON n.nid = fdfd.entity_id AND n.vid = fdfd.revision_id LEFT JOIN field_data_field_designation fdfdn ON n.nid = fdfdn.entity_id AND n.vid = fdfdn.revision_id LEFT JOIN field_data_field_email fdfe ON n.nid = fdfe.entity_id AND n.vid = fdfe.revision_id LEFT JOIN field_data_field_external_link fdfel ON n.nid = fdfel.entity_id AND n.vid = fdfel.revision_id LEFT JOIN field_data_field_file_image_alt_text fdffiat ON n.nid = fdffiat.entity_id AND n.vid = fdffiat.revision_id LEFT JOIN field_data_field_file_image_title_text fdffitt ON n.nid = fdffitt.entity_id AND n.vid = fdffitt.revision_id LEFT JOIN field_data_field_lead_news_behavior fdflnb ON n.nid = fdflnb.entity_id AND n.vid = fdflnb.revision_id LEFT JOIN field_data_field_news_body fdfnb ON n.nid = fdfnb.entity_id AND n.vid = fdfnb.revision_id LEFT JOIN field_data_field_publish_date fdfpd ON n.nid = fdfpd.entity_id AND n.vid = fdfpd.revision_id LEFT JOIN field_data_field_section_title fdfst ON n.nid = fdfst.entity_id AND n.vid = fdfst.revision_id LEFT JOIN field_data_field_shoulder fdfs ON n.nid = fdfs.entity_id AND n.vid = fdfs.revision_id LEFT JOIN field_data_field_sub_headline fdfsh ON n.nid = fdfsh.entity_id AND n.vid = fdfsh.revision_id where n.type = 'news' and n.status = 1 order by n.nid desc"" limit %s,%s")

    for result in cursor.execute(query, (start, offset), multi=True):
        if result.with_rows:
            # print("Rows produced by statement '{}':".format(result.statement))
            rows = result.fetchall()
            for row in rows:
                news = process_row(row)
                squery = 'slug:' + news['slug']
                print(squery)
                news_response = search_news(squery)
                print(news_response)

                if news_response.status_code == 200:
                    news_found = news_response.json()
                    if len(news_found) < 1:
                        img_hash = upload_img(news['featuredImage'], news['id'])
                        news['featuredImage'] = img_hash

                        catQuery = (
                            "select fdfnc.entity_id, ttd.name, ttd.description from field_data_field_news_cat fdfnc LEFT JOIN taxonomy_term_data ttd ON ttd.tid = fdfnc.field_news_cat_tid where fdfnc.entity_id=%s"" limit %s,%s")

                        for cat_result in catCursor.execute(catQuery, (news.get('id'), 0, 3), multi=True):
                            if cat_result.with_rows:
                                # print("Rows produced by statement '{}':".format(cat_result.statement))
                                cat_rows = cat_result.fetchall()
                                for cat_row in cat_rows:
                                    (entity_id, cat_name, cat_description) = cat_row
                                    print('category: ', entity_id, cat_name, cat_description)
                                    cat_slug = cat_name.replace(' ', '-')

                                    cat_response = search_categories('slug:' + cat_slug + '+AND+title:' + cat_name)
                                    print(cat_response)

                                    if cat_response.status_code == 200:
                                        cats = cat_response.json()
                                        if len(cats) < 1:
                                            category = {
                                                "slug": cat_slug,
                                                "title": cat_name,
                                                "description": cat_description,
                                                "image": "",
                                                "language": "BN",
                                                "parentId": None,
                                                "parentSlug": "",
                                                "status": "DRAFT"
                                            }
                                            cat_create_result = create_category(category)
                                            if cat_create_result.status_code == 201:
                                                news.get('categories').append(cat_create_result.json())
                                        else:
                                            news.get('categories').append(cats[0])


                                            # else:
                                            # print("Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount))

                        del(news['id'])

                        if news.get('byline') == None:
                            news['byline'] = news['title']

                        if news.get('imageCaption') == None:
                            news['imageCaption'] = news['title']

                        print('Publishing news: %s' % news)


                        cnews_response = create_news(news)
                        print(cnews_response)
                        if cnews_response.status_code == 201:
                            print('news created', cnews_response.json().get('slug'))

                    else:
                        print('news with slug %s already exists' % news.get('slug'))

    cursor.close()
    catCursor.close()
    cnx.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', help='start', type=int)
    parser.add_argument('-o', '--offset', help='offset', type=int)

    try:
        args = parser.parse_args()
        if args.start is None:
            args.start = 0
        if args.offset is None:
            args.offset = 10
        log.ok('running... with options: %s ' % args)
        run(args.start, args.offset)
    except:
        raise
        parser.print_help()
