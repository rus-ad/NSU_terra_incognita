from abc import ABCMeta, abstractmethod


class IKnowledgeBase(metaclass = ABCMeta):

    @abstractmethod
    def find_obj(self, obj_name : str):
        pass