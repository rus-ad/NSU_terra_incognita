from servives.maze_objects.cell import Cell
from servives.user import IUser


class Empty(Cell):

    def __init__(self, name: int, description: str, user_is_here: bool=False):
        mask = ' '
        Cell.__init__(self, name, description, mask, user_is_here)

    def user_has_action(self, user: IUser) -> bool:
        return True


class Jewel(Cell):

    def __init__(self, name: int, description: str, user_is_here: bool=False):
        mask = 'J'
        Cell.__init__(self, name, description, mask, user_is_here)

    def user_has_action(self, user: IUser) -> bool:
        user.jewel = True
        return True


class Output(Cell):

    def __init__(self, name: int, description: str, user_is_here: bool=False):
        mask = 'O'
        Cell.__init__(self, name, description, mask, user_is_here)

    def user_has_action(self, user: IUser) -> bool:
        if user.user_has_jewel():
            self.state = True
            return True
        return False


class River(Cell):

    def __init__(self, name: int, description: str, end_river: list, user_is_here: bool=False):
        mask = '~'
        Cell.__init__(self, name, description, mask, user_is_here)
        self.end_point = end_river

    def user_has_action(self, user: IUser) -> bool:
        return True


class Wall(Cell):

    def __init__(self, name: int, description: str):
        mask = '#'
        Cell.__init__(self, name, description, mask)

    def user_has_action(self, user: IUser) -> bool:
        return False