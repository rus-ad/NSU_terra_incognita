from impl.knowledge_base import make_algorithm_dict, KnowledgeBase
from servives.notion import INotion
from servives.maze_objects.object_storage import *

import matplotlib.pyplot as plt
from numpy.random import randint as rand
import numpy as np


class Labyrinth(INotion):

    def __init__(self, left: int, right: int, type_algorithms: str='Prima'):
        self.__left = left
        self.__right = right
        self.__type = type_algorithms
        self.__name = 'Labirint'
        self.__description = 'Some Labirint'

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_image_of_labyrinth(self):
        arr = self.map.data.astype(int)
        plt.figure(figsize=(10, 5))
        plt.imshow(arr, cmap=plt.cm.binary, interpolation='nearest')
        plt.xticks([]), plt.yticks([])
        plt.savefig('image_of_labyrinth.png')

    def generate_output(self):
        points = []
        points.extend([[row, col] for row in [0, -1] for col in range(self.__left + 1)])
        points.extend([[row, col] for row in [0, -1] for col in range(self.__right + 1)])
        points = [point for point in points if point not in [
            [0, 0],
            [self.__left, self.__right],
            [0, self.__right],
            [self.__left, 0]
        ]]
        point = points[rand(0, len(points) - 1)]
        x, y = point
        self.map.data[x, y] = Output(10, 'Some output, if you got jewel')

    def create_river(self):
        len_riwer = int(round(self.__left / 4, 0))
        start_river = int(round(self.__left / 3, 0))
        x , y = [rand(start_river, self.__left), rand(start_river, self.__right)]
        step_x = 1 if (x + len_riwer) < self.__left else -1
        step_y = 1 if (y + len_riwer) < self.__right else -1

        river_points = [[x, y]]
        for _ in range(len_riwer):
            x += np.random.choice([0, step_x], p=[0.5, 0.5])
            y += np.random.choice([0, step_y], p=[0.5, 0.5])
            river_points.append([x, y])

        for x, y in river_points:
            self.map.data[x, y] = River(7, 'You hit the river!', river_points[-1])


    def get_start_point(self):
        arr_x, arr_y = np.where(self.map.data == 0)
        shape = round((len(arr_x) - 1) / 2, 0)
        rand_user_point = rand(0, shape)
        rand_jewel_point = rand(shape, len(arr_x) - 1)
        x, y = arr_x[rand_user_point], arr_y[rand_user_point]
        self.start_point = [x, y]
        self.map.data[x, y] = Empty(0, 'Place is free', user_is_here=True)
        self.map.data[arr_x[rand_jewel_point], arr_y[rand_jewel_point]] = Jewel(
            9,
            'You found a treasure! Time to get out of this maze.'
        )

    def init_other_objects_map(self):
        wall_x, wall_y = np.where(self.map.data == 1)
        for x, y in zip(wall_x, wall_y):
            self.map.data[x, y] = Wall(1, 'This is wall')

        empty_x, empty_y = np.where(self.map.data == 0)
        for x, y in zip(empty_x, empty_y):
            self.map.data[x, y] = Empty(0, 'Place is free')

    def create_map(self):
        algorithm_by_obj = make_algorithm_dict()
        base = KnowledgeBase(algorithm_by_obj)
        self.map = base.find_obj(self.__type)
        self.map.generate(self.__left, self.__right)
        self.get_image_of_labyrinth()
        self.create_river()
        self.generate_output()
        self.get_start_point()
        self.init_other_objects_map()
