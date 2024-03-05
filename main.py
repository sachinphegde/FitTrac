#!/usr/bin/env python3
from flask import Flask
from auth.auth_app import auth

app = Flask(__name__)

app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(debug=True)

