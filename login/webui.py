#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database (replace this with your actual user database)
users = {
    'john': 'password123',
    'emma': 'abc123',
    'alice': 'qwerty'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Authentication successful
        # Here you would typically set up a session for the user
        return redirect(url_for('success'))
    else:
        # Authentication failed
        return render_template('login.html', message='Invalid username or password')

@app.route('/success')
def success():
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True)