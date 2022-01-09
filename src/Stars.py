import dataclasses
from src.GetData import GetData


@dataclasses.dataclass
class Stars(GetData):
    _all_stars: int = 0

    def to_dict(self) -> dict:
        return {
            'user': self.user,
            'all_stars': self.all_stars
        }

    def count_stars(self) -> None:
        count = 0
        for repo in self.repos:
            count += repo["stars"]
        self.all_stars = count

    @property
    def all_stars(self):
        return self._all_stars

    @all_stars.setter
    def all_stars(self, value):
        self._all_stars = value
