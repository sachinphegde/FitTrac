from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dummy database for storing user credentials (you would typically use a real database)
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        # Authentication successful, redirect to home page or dashboard
        return redirect(url_for('home'))
    else:
        # Authentication failed, redirect back to login page with error message
        return redirect(url_for('index', error='Invalid username or password'))

@app.route('/signup', methods=['POST'])
def signup():
    new_username = request.form['new_username']
    new_password = request.form['new_password']
    if new_username in users:
        # Username already exists, redirect back to signup page with error message
        return redirect(url_for('index', error='Username already exists'))
    else:
        # Registration successful, add new user to the database
        users[new_username] = new_password
        # Optionally, you may redirect the user to the login page or a success page
        return redirect(url_for('index'))

@app.route('/home')
def home():
    return 'Welcome to the home page'

if __name__ == '__main__':
    app.run(debug=True)
