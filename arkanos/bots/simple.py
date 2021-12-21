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
    pass  # TODO
