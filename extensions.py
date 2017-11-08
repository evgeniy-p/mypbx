import requests
import json
import myexception

host = 'https://apiproxy.telphin.ru/api/ver1.0'

class Exten:
    def __init__(self, menuform):
        self.menuform = menuform
        self.extbody = {
            "caller_id_name": None,
            "dial_rule_limit": 0,
            "did_as_transfer_caller_id": None,
            "extension_group_id": 0,
            "extra_params": None,
            "from_public_caller_id_number": True,
            "label": None,
            "name": None,
            "public_caller_id_number": None,
            "rfc_public_caller_id_number": True,
            "status": "active",
            "type": "phone"
        }

    def get_all_extensions(self, **kwargs):
        payload = kwargs
        answ= requests.get(host+'/client/{client_id}/extension/'.format(client_id=self.menuform.clientinfo.clientinfo['id']),
                            headers=self.menuform.loginform.take_auth_header(), params=payload)
        return json.loads(answ.content)

    def add_extension(self, name=None):
        if not name:
            raise myexception.extension_name_must_be_set
        else:
            self.extbody['name'] = name
        answer = requests.post('https://apiproxy.telphin.ru/api/ver1.0/client/{client_id}/extension/',
                               headers=self.menuform.loginform.take_auth_header(), data=self.extbody)
        return json.loads(answer.content)

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
                               headers=self.menuform.loginform.take_auth_header())
        return answer




