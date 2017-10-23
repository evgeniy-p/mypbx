import requests
import json
import gettoken

"""
id = id

secret = secret

"""

class Exten:
    def __init__(self):
        self.tokenreturn = gettoken.Token('id', 'secret')

    def all_extensions(self):
        pass

    def take_auth_header(self):
        return {'Authorization': 'Bearer {token}'.format(token=self.tokenreturn.get_token())}

    def get_all_extensions(self):
        pass

    def add_extension(self):
        pass

    def del_extension(self):
        pass

    def get_extension(self):
        pass

    def update_extension(self):
        pass

    def get_all_groups(self):
        pass

    def add_group(self):
        pass

    def del_group(self):
        pass

    def get_group(self):
        pass

    def update_group(self):
        pass

    def get_registrations(self):
        answer = requests.get('https://apiproxy.telphin.ru/api/ver1.0/extension/registration',
                               headers=self.take_auth_header())
        return answer


if __name__ == "__main__":
    check = Exten()
    print(json.loads(check.get_registrations().content))




