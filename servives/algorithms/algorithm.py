from abc import ABCMeta, abstractmethod
import numpy as np
from servives.notion import INotion


class IAlgorithm(INotion, metaclass=ABCMeta):

    @abstractmethod
    def generate(self, left: int, right: int, complexity: float=.75, density: float=.75) -> np.ndarray:
        pass