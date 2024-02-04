from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify({'message': 'Hello, API!'})

if __name__ == '__main__':
    app.run(debug=True)






#------------------- to have multiple apis running ----------------------------
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/contact')
def contact():
    return 'Contact Page'

if __name__ == '__main__':
    app.run(debug=True)