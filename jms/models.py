#! coding: utf-8

import datetime


class Decoder:
    @classmethod
    def from_json(cls, json_dict):
        self = cls()
        for k, v in json_dict.items():
            if isinstance(getattr(self, k, None), datetime.datetime):
                v = datetime.datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
            setattr(self, k, v)
        return self

    @classmethod
    def from_multi_json(cls, json_dict_list):
        return [cls.from_json(json_dict) for json_dict in json_dict_list]


class User(Decoder):
    id = 0
    username = ""
    name = ""
    email = ""
    is_active = False
    is_superuser = False
    role = "User"
    groups = []
    wechat = ""
    phone = ""
    comment = ""
    date_expired = datetime.datetime.now()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Asset(Decoder):
    id = 0
    hostname = ""
    ip = ""
    port = 22
    system_users_granted = []
    is_active = False
    system_users_join = ""

    @classmethod
    def from_json(cls, json_dict):
        system_users_granted = SystemUser.from_multi_json(json_dict["system_users_granted"])
        json_dict["system_users_granted"] = system_users_granted
        return super().from_json(json_dict)

    def __str__(self):
        return self.hostname

    def __repr__(self):
        return self.hostname


class SystemUser(Decoder):
    id = 0
    name = ""
    username = ""
    protocol = "ssh"
    auth_method = "P"
    comment = ""
    password = ""
    private_key = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name