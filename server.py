#Import modules
from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

#Direct to root
@app.route('/')
def index():
    return app.send_static_file('index.html')

#Runs programe when called
if __name__ == "__main__":
    app.run(debug=True)