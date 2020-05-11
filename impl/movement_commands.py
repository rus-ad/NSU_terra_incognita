from servives.commands import IUserCommand
from servives.notion import INotion
from servives.maze_objects.object_storage import Empty


class IUserMovementCommand(INotion, IUserCommand):

    def __init__(self, name, description, bias_x, bias_y):
        self.bias_x, self.bias_y = bias_x, bias_y
        self.__name = name
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def evaluate(self, game) -> [str, bool]:
        if game.session.locking:
            return f"Use quick commands. There is no active gaming session.\n{game.session.quick_commands}", False

        curr_x, curr_y = game.session.user.currency_point
        x, y = curr_x + self.bias_x, curr_y + self.bias_y
        interaction_obj = game.session.labyrinth.map.data[x, y]
        curr_obj = game.session.labyrinth.map.data[curr_x, curr_y ]
        user_has_action = interaction_obj.user_has_action(game.session.user)
        user_state = interaction_obj.state

        if not user_has_action:
            return interaction_obj.get_description(), user_state

        if interaction_obj.get_name() == 9:
            game.session.labyrinth.map.data[x, y] = Empty(0, 'Place is free')

        if interaction_obj.__dict__.get('end_point', None):
            x, y = interaction_obj.end_point

        obj = game.session.labyrinth.map.data[x, y]
        curr_obj.user_is_here = False
        obj.user_is_here = True
        game.session.user.currency_point = [x, y]
        return f'Step has been taken: {interaction_obj.get_description()}', user_state


class Left(IUserMovementCommand):

    def __init__(self, description):
        self.bias_x, self.bias_y = [0, -1]
        name = self.get_command_tag()
        IUserMovementCommand.__init__(self, name, description, self.bias_x, self.bias_y)

    def get_command_tag(self) -> str:
        return 'left'

    def get_args_count(self) -> int:
        return 0


class Right(IUserMovementCommand):

    def __init__(self, description):
        self.bias_x, self.bias_y = [0, 1]
        name = self.get_command_tag()
        IUserMovementCommand.__init__(self, name, description, self.bias_x, self.bias_y)

    def get_command_tag(self) -> str:
        return 'right'

    def get_args_count(self) -> int:
        return 0


class Up(IUserMovementCommand):

    def __init__(self, description):
        self.bias_x, self.bias_y = [-1, 0]
        name = self.get_command_tag()
        IUserMovementCommand.__init__(self, name, description, self.bias_x, self.bias_y)

    def get_command_tag(self) -> str:
        return 'up'

    def get_args_count(self) -> int:
        return 0


class Down(IUserMovementCommand):

    def __init__(self, description):
        self.bias_x, self.bias_y = [1, 0]
        name = self.get_command_tag()
        IUserMovementCommand.__init__(self, name, description, self.bias_x, self.bias_y)

    def get_command_tag(self) -> str:
        return 'down'

    def get_args_count(self) -> int:
        return 0
