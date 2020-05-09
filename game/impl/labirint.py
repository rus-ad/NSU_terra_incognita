from .knowledge_base import make_algorithm_dict, KnowledgeBase
from servives.notion import INotion


class Labirint(INotion):

    def __init__(self, left, right):
        self.__left = left
        self.__right = right
        self.__type = 'Prima'
        self.__name = name
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_map(self):
        algorithm_by_obj = make_algorithm_dict()
        base = KnowledgeBase(algorithm_by_obj)
        self.map = base.find_obj(self.__type)
        self.map.generate(self.__left, self.__right)