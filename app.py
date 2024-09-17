# app.py
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_fact')
def get_fact():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    if response.status_code == 200:
        return response.json()['value']
    else:
        return "Failed to fetch a Chuck Norris fact. Please try again."

if __name__ == '__main__':
    app.run(debug=True)

