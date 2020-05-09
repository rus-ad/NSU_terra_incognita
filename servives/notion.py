from abc import ABCMeta, abstractmethod


class INotion(metaclass = ABCMeta):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_description(self):
        pass