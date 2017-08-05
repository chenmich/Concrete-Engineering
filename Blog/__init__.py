from flask import Blueprint, Flask
from Blog.views import index, post_by_author, post_body, post_editor
from flask_bootstrap import Bootstrap
from Blog import config

def __addurlrule(blogblueprint):
    blogblueprint.add_url_rule('/', endpoint=None, view_func=index)
    blogblueprint.add_url_rule('/post/<string:author>', view_func=post_by_author)
    blogblueprint.add_url_rule('/post/<int:Id>', view_func=post_body)
    blogblueprint.add_url_rule('/post/editor/<int:Id>', view_func=post_editor)
#
def create_blueprint():
    blog_blueprint = Blueprint('blog', __name__,
                               template_folder='templates',
                               static_folder='static')
#
    __addurlrule(blog_blueprint)
    return blog_blueprint
#
def init_app(app, config_name):
    bootstrap = Bootstrap(app)
    if  not isinstance(app, Flask):
        raise TypeError('app is not an instance of class Flask')
    blog_blue= create_blueprint()
    blog_blue.static_url_path=app.static_url_path + "/blog"
    app.register_blueprint(blog_blue)
    app.config.from_object(config.config[config_name])
    config.config[config_name].init_app(app)
    
