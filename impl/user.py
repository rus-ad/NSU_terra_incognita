from servives.user import IUser

import http.client


class User(IUser):

    def __init__(self, start_point: list):
        self.name = self.get_user_name()
        self.__description = 'Some user'
        self.jewel = False
        self.currency_point = start_point

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.__description

    def get_user_name(self) -> str:
        conn = http.client.HTTPConnection("ifconfig.me")
        conn.request("GET", "/ip")
        return conn.getresponse().read().decode('utf-8')

    def user_has_jewel(self) -> bool:
        return self.jewel
