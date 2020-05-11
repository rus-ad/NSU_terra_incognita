import time

from impl.labyrinth import Labyrinth
from impl.user import User
from servives.notion import INotion


class Session(INotion):

    def __init__(self):
        self.datetime = round(time.time(), 0)
        self.__name = int(self.datetime)
        self.__description = f'Session: {self.__name} \n' \
                             f'Time: {time.ctime(self.datetime)} \n'
        self.locking = True

    def get_name(self) -> int:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def create_labyrinth(self, left: int, right: int):
        self.labyrinth = Labyrinth(left, right)
        self.labyrinth.create_map()
        self.user = User(self.labyrinth.start_point)




