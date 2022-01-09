import dataclasses
from src.Data import Data
import requests
from flask import abort, make_response, jsonify
import os


@dataclasses.dataclass
class GetData:
    _user: str
    _repos = []

    def to_dict(self) -> dict:
        return {
            "user": self.user,
            "repos": self.repos
        }

    def get_data(self) -> None:
        page_num = 1
        self.repos = []
        while True:
            try:
                headers = {}
                if os.environ["TOKEN"] != '':
                    headers = {'Authorization': f'Token {os.environ["TOKEN"]}'}
                url = f"https://api.github.com/users/{self.user}/repos?page={page_num}&per_page=100"
                response = requests.get(url, headers=headers)
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                res = {
                    "code": response.status_code,
                    "name": requests.status_codes._codes[response.status_code][0],
                    "description": response.reason,
                    "source": "GitHub API"
                }
                abort(response.status_code, res)
            else:
                if response.json():
                    for r in response.json():
                        data = Data(r.get("name"), r.get("stargazers_count"))
                        self.repos.append(data.to_dict())
                    page_num += 1
                else:
                    break


    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        self._user = value

    @property
    def repos(self):
        return self._repos

    @repos.setter
    def repos(self, value):
        self._repos = value


