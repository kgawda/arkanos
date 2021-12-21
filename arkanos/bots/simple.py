import random

from abc import ABC, abstractmethod


class BaseBot(ABC):
    @abstractmethod
    def select_action(self):
        pass


class DoNotihngBot(BaseBot):
    def select_action(self):
        return ('pass', (0, 0))


class RandomWalk(BaseBot):
    def select_action(self):
        delta = random.choice((1, -1))
        if random.randint(0, 1):  # czy w poziomie
            xy = (delta, 0)
        else:
            xy = (0, delta)
        return ('move', xy)
