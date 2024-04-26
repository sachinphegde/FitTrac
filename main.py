#!/usr/bin/env python3
from flask import Flask
from auth.auth_app import auth
from database import database
#from login.login_app import login

app = Flask(__name__)

app.register_blueprint(auth)
#login.register_blueprint(login)

def main():
    #initialize the database
    database.create_database('fitTrac')
    #run the application
    app.run(debug=True)


if __name__ == '__main__':
    main()
