from flask import Flask
from flask_bootstrap import Bootstrap
from Blog import create_blueprint

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.register_blueprint(create_blueprint())

if __name__ == '__main__':
    app.run(debug=True)