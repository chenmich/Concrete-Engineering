from flask import Blueprint
from flask_bootstrap import Bootstrap
from .views import login, logout

def __create_blueprint():
    auth  = Blueprint(
                "auth",
                __name__,
                template_folder="templates",
                static_folder="static"            
            )
    auth.add_url_rule("/loging", endpoint=None, view_func=login, methods=['POST'])
    auth.add_url_rule("/logout", endpoint=None, view_func=logout)
    return auth
auth = __create_blueprint()

class FlaskAuth():

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)
        else:
            self.__app = None
    
    def init_app(self, app):
        self.__app = app
        auth.static_url_path = static_url_path=app.static_url_path + "auth"
        self.__add__bootstrap__(app)
        app.register_blueprint(auth)
    
    def __add__bootstrap__(self, app):
        some = 'bootstrap' in  app.blueprints
        if some  is not True:
            Bootstrap(app)