from abc import ABCMeta, abstractmethod


class IUserCommand(metaclass=ABCMeta):

    @abstractmethod
    def get_command_tag(self) -> str:
        pass

    @abstractmethod
    def get_args_count(self) -> int:
        pass


