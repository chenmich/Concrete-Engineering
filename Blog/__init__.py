from flask import Blueprint, Flask
from .views import index
from flask_bootstrap import Bootstrap
from.config import config


def create_blueprint():
    blog_blueprint = Blueprint('blog', __name__,
                               template_folder='templates',
                               static_folder='static')
  
    blog_blueprint.add_url_rule('/', endpoint=None, view_func=index)
    return blog_blueprint

def init_app(app):
    bootstrap = Bootstrap(app)
    if  not isinstance(app, Flask):
        raise TypeError('app is not an instance of class Flask')
    app.register_blueprint(create_blueprint())


