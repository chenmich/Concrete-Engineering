from flask import Flask
from Blog.flask_auth import FlaskAuth
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

FlaskAuth(app)


@app.route('/')
def index():
    return "OK!!!"

if __name__ == "__main__":
    app.run(debug=True)