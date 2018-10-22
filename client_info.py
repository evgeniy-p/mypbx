import requests
import json
import myexception


class Client:
    def __init__(self, classwithtoken):
        answer = requests.get('https://{apihost}/api/ver1.0/user/'.format(apihost=classwithtoken.api_host),
                              headers=classwithtoken.take_auth_header())
        if answer.status_code == 429:
            raise myexception.rate_limit_exceeded
        answer = json.loads(answer.content.decode('ascii'))
        self.user_info = answer
        self.client_id = answer["client_id"]
        self.extension_group_id = answer["extension_group_id"]
        self.extension_id = answer["extension_id"]
        self.read_only_stat = answer["access"]
        answer = requests.get('https://{apihost}/api/ver1.0/client/{client_id}/client/'
                              ''.format(apihost=classwithtoken.api_host, client_id=self.client_id),
                              headers=classwithtoken.take_auth_header())
        answer = json.loads(answer.content.decode('ascii'))
        self.clientinfo = answer
        answer = requests.get('https://{apihost}/api/ver1.0/client/{client_id}/disk_space/'
                              .format(apihost=classwithtoken.api_host, client_id=self.client_id),
                              headers=classwithtoken.take_auth_header())
        self.disk_space_info = json.loads(answer.content.decode('ascii'))
        userpayload = {'login': self.user_info['login']}
        answer = requests.get('https://{apihost}/api/ver1.0/client/{client_id}/user/client/'
                              .format(apihost=classwithtoken.api_host, client_id=self.client_id),
                              params=userpayload, headers=classwithtoken.take_auth_header())
        self.user_name = json.loads(answer.content.decode('ascii'))[0]