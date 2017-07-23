from flask import Blueprint
from .views import index
from flask_bootstrap import Bootstrap


def create_blueprint():
    blog_blueprint = Blueprint('blog', __name__,
                               template_folder='templates',
                               static_folder='static')
    
    blog_blueprint.add_url_rule('/', endpoint=None, view_func=index)
    return blog_blueprint
