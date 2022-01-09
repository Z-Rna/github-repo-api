# from route import app, jsonify
from src import app
from flask import  jsonify
from werkzeug.exceptions import HTTPException

@app.errorhandler(HTTPException)
def error_handler_HTTP(e):
    response= jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
        "source": "Server application: HTTP error"
    })
    response.status_code = e.code
    return response

@app.errorhandler(Exception)
def error_handler_python(e):
    print(e)
    response = jsonify({
        "code": 500,
        "name": "Internal Server Error",
        "description": "The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.",
        "source": "Server application: python error"
    })
    response.status_code = 500
    return response