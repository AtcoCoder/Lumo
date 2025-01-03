"""Home route module"""
from web_flask.run import app
from flask import render_template


@app.route('/', strict_slashes=False)
def home():
    return render_template('index.html')

@app.route(
    '/login',
    strict_slashes=False,
    methods=['GET', 'POST']
)
def login():
    """login page"""
    return 'Login'


@app.route(
    '/signup',
    strict_slashes=False,
    methods=['POST', 'GET']
)
def signup():
    """signup page"""
    return 'Sign Up'
