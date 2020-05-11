from servives.commands import IUserCommand
from servives.notion import INotion
import pickle
import os


class IUserHigtLevelCommand(INotion, IUserCommand):

    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description


class Start(IUserHigtLevelCommand):

    def __init__(self, description):
        name = self.get_command_tag()
        IUserHigtLevelCommand.__init__(self, name, description)

    def get_command_tag(self) -> str:
        return 'start'

    def get_args_count(self) -> int:
        return 2

    def evaluate(self, left, right, game) -> [str, bool]:
        game.session.locking = False
        game.session.create_labyrinth(int(left), int(right))
        return "Game started", False


class Save(IUserHigtLevelCommand):

    def __init__(self, description):
        name = self.get_command_tag()
        IUserHigtLevelCommand.__init__(self, name, description)

    def get_command_tag(self) -> str:
        return 'save'

    def get_args_count(self) -> int:
        return 0

    def evaluate(self, game) -> [str, bool]:
        if game.session.locking: return "The game is not running!", False

        filename = game.session.get_name()
        with open(f'save/{filename}.pckl', 'wb') as file:
            pickle.dump(game.session, file)
        return "Game saved successfully", False


class Exit(IUserHigtLevelCommand):

    def __init__(self, description):
        name = self.get_command_tag()
        IUserHigtLevelCommand.__init__(self, name, description)

    def get_command_tag(self) -> str:
        return 'exit'

    def get_args_count(self) -> int:
        return 0

    def evaluate(self, game) -> [str, bool]:
        return "Good bay!", True


class Load(IUserHigtLevelCommand):

    def __init__(self, description):
        name = self.get_command_tag()
        IUserHigtLevelCommand.__init__(self, name, description)

    def get_command_tag(self) -> str:
        return 'load'

    def get_args_count(self) -> int:
        return 0

    def evaluate(self, game) -> [str, bool]:
        os.system('cls' if os.name == 'nt' else 'clear')
        saves = os.listdir('save/')
        for i, save in enumerate(saves):
            print(f'{i}: {save}')

        try:
            num_save = int(input('Enter the save number to download: '))
        except:
            return "The number must be a number!", False

        if num_save >= len(saves):
            return "Saving game not found under this number!", False

        with open(f'save/{saves[num_save]}', 'rb') as file:
            game.session = pickle.load(file)

        game.session.locking = False
        return "Game loaded successfully", False