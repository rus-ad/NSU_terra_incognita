from abc import ABCMeta, abstractmethod


class Session(metaclass=ABCMeta):

    @abstractmethod
    def descripton(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def exit(self):
        pass