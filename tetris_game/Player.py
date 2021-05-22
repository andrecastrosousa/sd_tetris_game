
class Player:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    @property
    def name(self) -> str:
        return self._name