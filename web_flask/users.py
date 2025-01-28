"""User authentication and Management routes"""
from web_flask.run import app



@app.route('/auth/login', methods=['GET', 'POST'])
def user_login():
    """User login route"""
    pass