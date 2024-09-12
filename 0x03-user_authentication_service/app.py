#!/usr/bin/env python3
'''Flask app'''

from auth import Auth
from flask import Flask, jsonify, request, redirect


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"], strict_slashes=False)
def mess() -> str:
    '''return defined payload'''
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """POST /users
    Return:
        The account creation process reponse
    """
    email, password = request.form.get("email"), request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    '''POST /sessions
        Return:
        The session creation process reponse
    '''

    email, password = request.form.get("email"), request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response

    else:
        Flask.abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    '''Delete /sessions
        Return:
        The session deletion process reponse
    '''
    session_id = request.cookies.get("session_id")
    if AUTH.destroy_session(session_id):
        Auth.destroy_session(session_id)
        return redirect('/')
    Flask.abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
