"""Home route module"""
from web_flask.run import app
from flask import render_template


@app.route('/', strict_slashes=False)
def home():
    return render_template('index.html')
