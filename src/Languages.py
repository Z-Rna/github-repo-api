# from src import GetData
from src.GetData import GetData
import requests
from flask import abort, make_response, jsonify
import dataclasses
import os

@dataclasses.dataclass
class Languages(GetData):
    _languages = {}

    def to_dict(self) -> dict:
        return {
            'user': self.user,
            'languages': self.languages
        }

    def get_languages_info(self):
        self.languages = {}
        for repo in self.repos:
            try:
                headers = {}
                if os.environ["TOKEN"] != '':
                    headers = {'Authorization': f'Token {os.environ["TOKEN"]}'}
                url = f"https://api.github.com/repos/{self.user}/{repo['name']}/languages"
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
                    sorted_response = dict(sorted(response.json().items(),
                                              key=lambda item: item[1],
                                              reverse=True))
                    key, value = list(sorted_response.items())[0]
                    if key not in self.languages:
                        self.languages[key] = 0
                    self.languages[key] += value


    @property
    def languages(self):
        return self._languages

    @languages.setter
    def languages(self, value):
        self._languages = value