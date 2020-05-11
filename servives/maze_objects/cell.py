from abc import ABCMeta, abstractmethod
from servives.notion import INotion
from servives.user import IUser


class ICell(INotion, metaclass=ABCMeta):

    @abstractmethod
    def get_mask(self) -> str:
        pass

    @abstractmethod
    def user_has_action(self, user: IUser):
        pass


class Cell(ICell):

    def __init__(self, name: int, description: str, mask: str, user_is_here: bool=False):
        self.__name = name
        self.__description = description
        self.state = False
        self.__mask = mask
        self.user_is_here = user_is_here

    def get_name(self) -> int:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def user_has_action(self, user: IUser):
        pass

    def get_mask(self) -> str:
        if self.user_is_here:
            return 'U'

        return self.__mask