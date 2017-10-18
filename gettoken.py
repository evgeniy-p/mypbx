import requests
import conf
import json
import myexception
from time import time


class Token:
    def __init__(self, apID, apSecret):
        self.apID = apID
        self.apSecret = apSecret
        self.token = None
        self.tokentime = None

    def get_token(self):
        if not self.token:
            self.new_token()
            return self.token
        else:
            if time() - self.tokentime > 3600:
                self.new_token()
                return self.token
            else:
                return self.token

    def new_token(self):
        payload = {'grant_type': 'client_credentials', 'client_id': self.apID, 'client_secret': self.apSecret}
        resouath = requests.post('https://apiproxy.telphin.ru/oauth/token', data=payload)
        if not resouath.ok:
            raise myexception.cant_get_OK_check_appid_and_secret
        self.token = json.loads(resouath.content)["access_token"]
        self.tokentime = time()
        return self.token


if __name__ == "__main__":
    ringme_token = Token(conf.APPID, conf.SECRET)
    print(ringme_token.get_token())

