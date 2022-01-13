# -*- coding: utf-8 -*-
# !/usr/bin/env python
import json
import requests
from bs4 import BeautifulSoup

token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIwNUxzNzRZbExZOUx0ZC0zaHNlaVZGbXZKZmlFUUpzUmVUcF8wVHJUWFJjIn0.eyJqdGkiOiIzNjU4Zjc2ZC05MDdjLTQ0MjktYTdhNy01MTQxNWE0NjA4OWYiLCJleHAiOjE1ODA0OTg0NTAsIm5iZiI6MCwiaWF0IjoxNTgwNDk4MTUwLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjkwODAvYXV0aC9yZWFsbXMvamhpcHN0ZXIiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiYTM1ZGVkZGQtNTI2OS00NzM1LTk2NjktNTBjNTVkZjcyNmRjIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViX2FwcCIsImF1dGhfdGltZSI6MTU4MDQ5ODE1MCwic2Vzc2lvbl9zdGF0ZSI6ImQ1N2RlMjBlLWJiMjctNDhjNC05ZjBmLTVhOTZjNjUzODc3NSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsiUk9MRV9VU0VSIiwib2ZmbGluZV9hY2Nlc3MiLCJST0xFX0FETUlOIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBqaGlwc3RlciBtaWNyb3Byb2ZpbGUtand0IGVtYWlsIG9mZmxpbmVfYWNjZXNzIHByb2ZpbGUgYWRkcmVzcyBwaG9uZSIsInVwbiI6ImZlcmRvdXMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYWRkcmVzcyI6e30sInJvbGVzIjpbIlJPTEVfVVNFUiIsIm9mZmxpbmVfYWNjZXNzIiwiUk9MRV9BRE1JTiIsInVtYV9hdXRob3JpemF0aW9uIl0sIm5hbWUiOiJOdXJ1bCBGZXJkb3VzIiwiZ3JvdXBzIjpbIlJPTEVfVVNFUiIsIm9mZmxpbmVfYWNjZXNzIiwiUk9MRV9BRE1JTiIsInVtYV9hdXRob3JpemF0aW9uIl0sInByZWZlcnJlZF91c2VybmFtZSI6ImZlcmRvdXMiLCJnaXZlbl9uYW1lIjoiTnVydWwiLCJmYW1pbHlfbmFtZSI6IkZlcmRvdXMiLCJlbWFpbCI6Im51cnVsQGZlcmRvLnVzIn0.ACCuGiqRcCUUuq3B0YsBm_XjEyfHryhSMoBjEVenzJK8DzcbHEOjiT4BgfG6h2CwYcBjlwqBMFAJdlpTu-DohVSe-cbawUcAx-3qLiDuR8aE3Rq6eDqQFnRnLBXKkrg7uxqOLFIZCOYFHqq9ZD-HKa2n7D47eWbgdp6sSGD_4avq-Da2X8pbpmuUZdOXdmQeNG4vy3uKYUUL51aZEtLFi_mZ9ujr1QGgCBtoVFB925kveGZQtNOJ75iiKsb1YU21SWYm0H6nBmWWJTOhequenYtEqq5XO7CkYf7j1jG8Lf-T9IdZBrDMggRtjeemA8Z-xETTyfxdsjdnorK5aEjBzg'


def get_categories(query):
    url = 'https://privatebeta.thedailystar.net/api/_search/categories?page=0&query=%s&size=2&sort=id,desc' % query

    payload = {}
    headers = {
        'Accept': 'text/json',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    response = requests.request('GET', url, headers=headers, data=payload)

    return response.json()


# print(get_categories('status:PUBLISHED'))

def create_news():
    url = 'https://privatebeta.thedailystar.net/api/news'

    payload = {
        'id': 5622,
        'title': 'Want to see democracy in action at Dhaka polls: Western diplomats',
        'slug': 'want-to-see-democracy-in-action-at-dhaka-polls-western-diplomats',
        'headline': 'Want to see democracy in action at Dhaka polls - Western diplomats',
        'featuredImage': 'c949db8090609fd79868731c4f6b9708',
        'imageCaption': 'Dhaka City Polls 2020',
        'highlight': '<p>Want to see democracy in action at Dhaka polls</p>',
        'subHead': 'Want to see democracy in action at Dhaka polls',
        'shoulder': 'Want to see democracy in action at Dhaka polls',
        'intro': 'Western diplomats in Dhaka said they want to see democracy in action as the Dhaka South and North City Corporation elections are going to be held day after tomorrow.',
        'content': '<p><strong>Western diplomats in Dhaka said they want to see democracy in action as the Dhaka South and North City Corporation elections are going to be held day after tomorrow.</strong></p><p>“The Dhaka City Corporation elections on 1 February are an opportunity for the citizens of Dhaka to exercise their democratic rights,” said a joint statement of nine diplomats posted on the UK High Commission’s Facebook page today evening.</p><p>“We look forward to seeing democracy in action in polling centres across the city,” they said.</p><p><br></p><p>They hope that the government of Bangladesh, the Election Commission and all political parties will respect the rights of citizens to cast their votes in a peaceful and festive atmosphere, and count the votes with fairness and integrity.</p><p>The signatories to the statement include Benoit Prefontaine, high commissioner of Canada; Charlotta Schlyter, ambassador of Sweden; Earl Miller, ambassador of United States; Robert Chatterton Dickson, High Commissioner of UK; Sidsel Bleken, ambassador of Norway; Winnie Estrup Petersen, ambassador of Denmark; Jeroen Steeghs, charge d’affairs of the Netherlands; Penny Morton, acting high commissioner of Australia and Suzanne Muller, charge d’affairs of Switzerland.</p>',
        'newsType': 'WEB',
        'newsLayout': 'DEFAULT',
        'byline': None,
        'liveEmbeddedCode': None,
        'publishDate': '2020-01-28T18:00:00Z',
        'hideAds': False,
        'commentable': False,
        'viewCount': 5,
        'language': 'EN',
        'status': 'PUBLISHED',
        'authorId': 1,
        'authorName': 'Staff Reporter',
        'relatedId': None,
        'relatedTitle': None,
        'magazineId': None,
        'magazineTitle': None,
        'locationId': None,
        'locationStreetAddress': None,
        'tags': [
            {
                'id': 1,
                'title': 'Random',
                'slug': 'random',
                'description': 'Random',
                'language': 'EN',
                'status': 'PUBLISHED'
            }
        ],
        'categories': [
            {
                'id': 6,
                'title': 'Country',
                'slug': 'country',
                'description': 'Country',
                'image': 'cd9717a0e1871e4262a3de53d3c7828a',
                'language': 'EN',
                'status': 'PUBLISHED',
                'parentId': 87,
                'parentSlug': 'bangladesh'
            },
            {
                'id': 75,
                'title': 'Careers',
                'slug': 'career',
                'description': 'Careers',
                'image': 'cd9717a0e1871e4262a3de53d3c7828a',
                'language': 'EN',
                'status': 'PUBLISHED',
                'parentId': 70,
                'parentSlug': 'life-living'
            }
        ],
        'newsOptions': [
            {
                'id': 1,
                'title': 'default',
                'slug': 'default',
                'description': 'default',
                'language': 'EN',
                'status': 'PUBLISHED'
            }
        ]
    }

    data = json.dumps(payload)
    print(type(data))
    print('\'' + data + '\'')

    headers = {
        'Accept': 'text/json',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJMbXVyX3M5N1BPS2k2ODZzTmZTTVFPamdJYjRqdVFEQm0zREVBZk15YzBjIn0.eyJqdGkiOiIwMjc3NmNjOC04YmMyLTQxYjAtOTQ3Yy00ZGFiMDA5ZjM5MjQiLCJleHAiOjE1ODA0NzUxMjAsIm5iZiI6MCwiaWF0IjoxNTgwNDc0ODIwLCJpc3MiOiJodHRwczovL3Nzby50aGVkYWlseXN0YXIubmV0L2F1dGgvcmVhbG1zL2poaXBzdGVyIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjQ2MDAxYWJkLTMxYjktNDc3MS1hMDM3LWExNGNlMDZmNTM4OSIsInR5cCI6IkJlYXJlciIsImF6cCI6IndlYl9hcHAiLCJhdXRoX3RpbWUiOjE1ODA0NzQyNTMsInNlc3Npb25fc3RhdGUiOiJhYTkzMGI4NS04YTA0LTQyNGEtYTFiNy0wNDYwMWY4YzJmY2IiLCJhY3IiOiIwIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIlJPTEVfVVNFUiIsIm9mZmxpbmVfYWNjZXNzIiwiUk9MRV9BRE1JTiIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgamhpcHN0ZXIgbWljcm9wcm9maWxlLWp3dCBlbWFpbCBvZmZsaW5lX2FjY2VzcyBwcm9maWxlIGFkZHJlc3MgcGhvbmUiLCJ1cG4iOiJmZXJkb3VzIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImFkZHJlc3MiOnt9LCJyb2xlcyI6WyJST0xFX1VTRVIiLCJvZmZsaW5lX2FjY2VzcyIsIlJPTEVfQURNSU4iLCJ1bWFfYXV0aG9yaXphdGlvbiJdLCJuYW1lIjoiTnVydWwgRmVyZG91cyIsImdyb3VwcyI6WyJST0xFX1VTRVIiLCJvZmZsaW5lX2FjY2VzcyIsIlJPTEVfQURNSU4iLCJ1bWFfYXV0aG9yaXphdGlvbiJdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJmZXJkb3VzIiwiZ2l2ZW5fbmFtZSI6Ik51cnVsIiwiZmFtaWx5X25hbWUiOiJGZXJkb3VzIiwiZW1haWwiOiJudXJ1bEBmZXJkby51cyJ9.HTRf8fAlKoCHxl6sXeSXzUicKaoMHNLO2GjT4eDq71bYbHK3brSNM6a1I6y_vGVOdFjKU_6rsMUDuYIheFHZQP4EfVTnv1ExKKaHr4N-ykiv78CPH_z33fkr6ngRORcNxrPkOXSjmdnQBV0FmCv-CoOLSUd9q2AyPpxwfLyLZ8KKC7DT_yA-K-uAtGEp3UAOiKeVmMsPlX_C0KffX38984GToD3HjCRJBjEJ_u2YoN6qwB1d1OG1TUjrHog5ckeYojb_G6A1G14v-zhPO0E7b2U9Acbf0oVd_-2VHOT2hKuLP5Zd3_ZKC0ezdMjJxaEnsvkcd2cubVRW8ZKqflZdAw'
    }
    response = requests.request('PUT', url, headers=headers, data=data)
    print(response)
    print(response.text.encode('utf8'))


def search_categories(query):
    url = 'http://localhost:8080/api/_search/categories?page=0&query=%s&size=2&sort=id,desc' % query
    print(url)

    payload = {}
    headers = {
        'Accept': 'text/json',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token
    }

    response = requests.request('GET', url, headers=headers, data=payload)
    return response.json()


def create_category(payload):
    url = 'http://localhost:8080/api/categories'

    headers = {
        'Accept': 'text/json',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token
    }

    data = json.dumps(payload)

    response = requests.request('POST', url, headers=headers, data=data)
    return response.json()


#
# cats = search_categories('slug:uncategorized+AND+title:Uncategorized')
# print(type(cats))
# print(len(cats))
# print(cats)
#
# category = {
#     'slug': 'uncategorized',
#     'title': 'uncategorized',
#     'description': 'uncategorized',
#     'image': '',
#     'language': 'BN',
#     'parentId': None,
#     'parentSlug': '',
#     'status': 'DRAFT'
# }
#
# if len(cats) < 1:
#     cat =  create_category(category)
#     print(cat)
# else:
#     print('category already exists %s' % category)

# HttpResponse<String> response = Unirest.post('https://img.thedailystar.net/upload')
#     .header('Accept', '*/*')
#     .header('Cache-Control', 'no-cache')
#     .header('Host', 'img.thedailystar.net')
#     .header('Accept-Encoding', 'gzip, deflate')
#     .header('Connection', 'keep-alive')
#     .header('cache-control', 'no-cache')
#     .field('userfille', file)
#     .asString();

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
        parsed_html = BeautifulSoup(result)
        hash = parsed_html.body.find('h1').text
        return hash


nid = 13097522
img_url = 'https://assetsds.cdnedge.bluemix.net/bangla/sites/default/files/feature/images/_f754916.jpg'
hash = upload_img(img_url, nid)
print(hash)
