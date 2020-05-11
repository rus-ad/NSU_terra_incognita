from abc import ABCMeta, abstractmethod
from servives.notion import INotion


class IUser(INotion, metaclass = ABCMeta):

    @abstractmethod
    def get_user_name(self) -> str:
        pass

    @abstractmethod
    def user_has_jewel(self) -> bool:
        pass
