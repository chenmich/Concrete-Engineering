from flask import Blueprint, Flask
from .views import index,user_post
from flask_bootstrap import Bootstrap
from.config import config

def __addurlrule(blogblueprint):
    blogblueprint.add_url_rule('/', endpoint=None, view_func=index)
    blogblueprint.add_url_rule('/post/<string:author>', view_func=user_post)

def create_blueprint():
    blog_blueprint = Blueprint('blog', __name__,
                               template_folder='templates',
                               static_folder='static')
  
    __addurlrule(blog_blueprint)
    return blog_blueprint

def init_app(app):
    bootstrap = Bootstrap(app)
    if  not isinstance(app, Flask):
        raise TypeError('app is not an instance of class Flask')
    app.register_blueprint(create_blueprint())


