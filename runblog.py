from flask import Flask
from Blog import create_blueprint, init_app

app = Flask(__name__)
init_app(app, "Development")

def main(app):
    app.run()

if __name__ == '__main__':
    main(app=app)
    