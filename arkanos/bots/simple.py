class BaseBot:
    def select_action(self):
        pass

class DoNotihngBot(BaseBot):
    def select_action(self):
        return ('pass', (0, 0))
