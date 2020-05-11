from impl.game_session import Session
from impl.knowledge_base import make_commands_dict, KnowledgeBase

import os
import sys
sys.path.append('terra_incognita/')


class Game:

    def __init__(self):
        self.game_has_end = False
        self.session = Session()
        name_by_commands = make_commands_dict()
        self.base = KnowledgeBase(name_by_commands)
        self.quick_commands = '''
            Quick Commands: 
            1) "start" to start the game;
            2) "load" to restore progress.
        '''
        self.message = self.quick_commands

    def action(self, user_input) -> [str, bool]:
        tokens = user_input.strip().split(" ")
        if not tokens:
            return 'Empty field', False

        norm_cmd = tokens[0].lower()
        args = tokens[1:10]
        self.cmd = self.base.find_obj(norm_cmd)
        if not self.cmd: return f"Command not supported: {norm_cmd}", False

        if self.cmd.get_args_count() != len(args):
            return f"Invalid number of args. Expected: {self.cmd.get_args_count()}, got: {len(args)}", False

        args += [self]
        return self.cmd.evaluate(*args)

    def game_in_process(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        if self.session.__dict__.get('labyrinth', None):
            for row in self.session.labyrinth.map.data:
                print('  '.join([obj.get_mask() for obj in row]))

        print(self.message)
        user_input = input('>>>')

        self.message, self.game_has_end = self.action(user_input)

    def game_passed(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.session.labyrinth.map.data:
            print('  '.join([obj.get_mask() for obj in row]))
        print('Happy end')

    def start(self):
        while not self.game_has_end:
            self.game_in_process()
        self.game_passed()


if __name__ == "__main__":
    some_game = Game()
    some_game.start()



