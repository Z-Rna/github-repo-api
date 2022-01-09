from src import app
from src.Stars import Stars
from src.Languages import Languages
from src.GetData import GetData
from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource
import os


blueprint = Blueprint('api', __name__)
api = Api(
    blueprint,
    default='',
    title='Github Repo Api',
    version='1.0',
    description='Get information about users repositories on Github',
    doc='/api',
    default_label='Options'
)


@app.route("/", methods=['GET'])
def home() -> dict:
    url = f'http://{request.headers.get("Host")}'
    return {
        'app info': 'implemented endpoints',
        'endpoints' : {
            'list of repositories for given user': {
                'endpoint': f'{url}/repos/{{user}}',
                'method': 'GET'
            },
            'count of stars for given user': {
                'endpoint': f'{url}/stars/{{user}}',
                'method': 'GET'
            },
            'list of used languages in repositories': {
                'endpoint': f'{url}/languages/{{user}}',
                'method': 'GET'
            },
            'GET github token': {
                'endpoint': f'{url}/token',
                'method': 'GET'
            },
            'DELETE github token': {
                'endpoint': f'{url}/token',
                'method': 'DELETE'
            },
            'POST github token': {
                'endpoint': f'{url}/token/{{token}}',
                'method': 'POST'
            },
            'swagger documentation': {
                'endpoint': f'{url}/api',
                'method': 'GET'
            },
        }
    }


app.register_blueprint(blueprint)

@api.route("/repos/<user>", methods=["GET"], doc={"description": "Get list of user's repositories"})
class RouteRepos(Resource):
    def get(self, user: str) -> dict:
        d = GetData(user)
        d.get_data()
        res = jsonify(d.to_dict())
        return res

@api.route("/stars/<user>", methods=["GET"], doc={"description": "Get number of stars for given user"})
class RouteStars(Resource):
    def get(self, user: str) -> dict:
        d = Stars(user)
        d.get_data()
        d.count_stars()
        res = jsonify(d.to_dict())
        return res

@api.route("/languages/<user>", methods=["GET"], doc={"description": "Get number of bytes for the most popular programing languages"})
class RouteLanguages(Resource):
    def get(self, user: str) -> dict:
        d = Languages(user)
        d.get_data()
        d.get_languages_info()
        res = jsonify(d.to_dict())
        return res

@api.route("/token", methods=["GET", "DELETE"], doc={"description": "Get authorization token"})
class RouteToken(Resource):
    def get(self) -> dict:
            return {
                "token": os.environ["TOKEN"]
            }
    def delete(self):
        os.environ["TOKEN"] = ''
        return {
            "info": "Token deleted",
            "token": os.environ["TOKEN"]
        }


@api.route("/token/<token>", methods=['POST'], doc={"description": "Post authorization token"})
class RouteSetToken(Resource):
    def post(self, token: str) -> dict:
        os.environ["TOKEN"] = token
        return {
            "info": "Posted token",
            "token": os.environ["TOKEN"]
        }
