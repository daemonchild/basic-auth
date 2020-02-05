from flask import Flask, render_template
from flask import request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "barry": "abc123",
    "beth": "xyz999"
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return users.get(username) == password
    return False


@auth.error_handler
def unauthorized():
    return render_template('display.html', action='Failed', username=auth.username(), headers = request.headers)


@app.route('/')

@auth.login_required
def index():

    return render_template('display.html', action='Successful', username=auth.username(), headers = request.headers)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8000)
