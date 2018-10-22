import requests
import conf
import json
import myexception
from time import time


class Token:
    def __init__(self):
        self.apID = conf.APPID
        self.apSecret = conf.SECRET
        self.redirect_uri = conf.URI
        self.api_host = conf.APIHOST
        self.token = None
        self.tokentime = None
        self.refresh_token = None

    def get_token(self, username=None, password=None):
        if not self.token:
            self.new_token(username, password)
            return self.token
        else:
            if time() - self.tokentime > 3600:
                self.do_refresh_token()
                return self.token
            else:
                return self.token

    def take_auth_header(self):
        return {'Authorization': 'Bearer {token}'.format(token=self.get_token())}

    def new_token(self, username, password):
        payload = {"username": username, "password": password}
        postbody = {'response_type': 'code', 'redirect_uri': self.redirect_uri, 'client_id': self.apID, 'scope': 'all'}
        with requests.Session() as req:
            answer = req.post('https://{apihost}/oauth/authorize'.format(apihost=self.api_host), params=postbody,
                              allow_redirects=False)
            answer = req.post(answer.headers['Location'], data=payload, allow_redirects=False)
            answer = req.get(answer.headers['Location'], cookies=req.cookies, allow_redirects=False)
        try:
            payload = {'grant_type': 'authorization_code', 'code': answer.headers['Location'].split('=')[1],
                       'client_id': self.apID, 'client_secret': self.apSecret, 'redirect_uri': self.redirect_uri}
        except BaseException:
            raise myexception.cant_get_OK_check_login_and_password
        resouath = requests.post('https://{apihost}/oauth/token'.format(apihost=self.api_host), data=payload)
        if not resouath.ok:
            raise myexception.cant_get_OK_check_login_and_password
        self.token = json.loads(resouath.content.decode('ascii'))["access_token"]
        self.refresh_token = json.loads(resouath.content.decode('ascii'))["refresh_token"]
        self.tokentime = time()
        return self.token

    def do_refresh_token(self):
        payload = {'grant_type': 'refresh_token', 'client_id': self.apID, 'client_secret': self.apSecret}
        resouath = requests.post('https://{apihost}/oauth/token'.format(apihost=self.api_host), data=payload)
        if not resouath.ok:
            raise myexception.cant_get_OK_need_recconect
        self.token = json.loads(resouath.content.decode('ascii'))["access_token"]
        self.refresh_token = json.loads(resouath.content.decode('ascii'))["refresh_token"]
        return self.token
