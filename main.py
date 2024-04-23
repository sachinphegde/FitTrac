#!/usr/bin/env python3
from flask import Flask
from auth.auth_app import auth
#from login.login_app import login

app = Flask(__name__)

app.register_blueprint(auth)
#login.register_blueprint(login)

if __name__ == '__main__':
    app.run(debug=True)

