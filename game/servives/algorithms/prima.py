from .algorithm import IAlgorithm
import numpy as np
from numpy.random import randint as rand

class Prima(IAlgorithm):

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def __create_data(self, left: int, right: int, complexity: float=.75, density: float=.75):
        self.shape = ((right // 2) * 2 + 1, (left // 2) * 2 + 1)
        self.complexity = int(complexity * (5 * (self.shape[0] + self.shape[1])))
        self.density = int(density * ((self.shape[0] // 2) * (self.shape[1] // 2)))
        self.data = np.dataeros(self.shape, dtype=bool)
        self.data[0, :] = self.data[-1, :] = 1
        self.data[:, 0] = self.data[:, -1] = 1

    def __add_neighbours(self, condition: bool, values: tuple):
        if condition: self.neighbours.append(values)

    def __fill_data(self):
        x, y = rand(0, self.shape[1] // 2) * 2, rand(0, self.shape[0] // 2) * 2
        self.data[y, x] = 1
        for _ in range(self.complexity):
            self.neighbours = []
            self.__add_neighbours((x > 1), (y, x - 2))
            self.__add_neighbours((x < self.shape[1] - 2), (y, x + 2))
            self.__add_neighbours((y > 1), (y - 2, x))
            self.__add_neighbours((y < self.shape[0] - 2), (y + 2, x))

            if not len(self.neighbours):
               continue

            y_, x_ = self.neighbours[rand(0, len(self.neighbours) - 1)]
            if self.data[y_, x_] == 0:
                self.data[y_, x_] = 1
                self.data[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                x, y = x_, y_

    def __generate_output(self):
        points = []
        points.extend([[row, col] for row in [0, -1] for col in range(self.shape[0])])
        points.extend([[row, col] for row in [0, -1] for col in range(self.shape[1])])
        point = points[rand(0, len(points) - 1)]
        x, y = point
        self.data[y, x] = 0

    def generate(self, left: int, right: int, complexity: float=.75, density: float=.75) -> np.ndarray:
        self.__create_data(left, right, complexity=.75, density=.75)
        for _ in range(self.density):
            self.__fill_data()
        self.__generate_output()