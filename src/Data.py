import dataclasses


@dataclasses.dataclass
class Data:
    _name: str = ""
    _stars: int = 0

    def to_dict(self):
        return {
            "name": self.name,
            "stars": self.stars,
        }

    @property
    def name(self):
        return self._name

    @name.setter
    def user(self, value):
        self._name = value

    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, value):
        self._stars = value
