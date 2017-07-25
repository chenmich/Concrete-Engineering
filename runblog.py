from flask import Flask

from Blog import create_blueprint, init_app

app = Flask(__name__)
init_app(app)
def main(app, mode):
    app.run(debug=mode)

if __name__ == '__main__':
    main(app=app, mode=True)
