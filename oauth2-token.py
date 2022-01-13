import json
import uuid

import requests

authorize_url = "http://localhost:9080/auth/realms/jhipster/protocol/openid-connect/auth"
token_url = "http://localhost:9080/auth/realms/jhipster/protocol/openid-connect/token"

# callback URL specified when the application was defined
callback_uri = "http://localhost:8080/login/oauth2/code/oidc"

test_api_url = "http://localhost:9080/api/account"

# client (application) credentials on apim.byu.edu
client_id = 'web_app'
client_secret = 'web_app'

# step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# prompted for credentials.

# http://localhost:9080/auth/realms/jhipster/protocol/openid-connect/auth?response_type=code&client_id=web_app&scope=openid%20address%20email%20jhipster%20microprofile-jwt%20offline_access%20phone%20profile%20roles%20web-origins&state=5xIlNcBApgCfVSsVhd8SnRSePdkt4Sqk9llAtBntwbc%3D&redirect_uri=http://localhost:8080/login/oauth2/code/oidc
authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid%20address%20email%20jhipster%20microprofile-jwt%20offline_access%20phone%20profile%20roles%20web-origins&state=' + uuid.uuid1().hex

print "go to the following url on the browser and enter the code from the returned url: "
print "---  " + authorization_redirect_url + "  ---"
authorization_code = raw_input('code: ')

# step I, J - turn the authorization code into a access token, etc
data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}
print "requesting access token"
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

print "response"
print access_token_response.headers
print 'body: ' + access_token_response.text

# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']
print "access token: " + access_token

api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)

print api_call_response.text
