from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import UserMixin


def User(UserMixin):
    def __init__(self, id=None, email=None, username=None, password_hash=None, role_id=None):
        self.__id = id 
        self.__email = email 
        self.__username = username
        self.__password_hash = password_hash 
        self.__role_id = role_id
        self.__is_active = False
        self.__is_authenticated = False
        self.__is_anonymous = False
        self.__avatar = None

    @property
    def get_id(self):
        return self.__id
    @property
    def is_authenticated(self):
        return self.__is_authenticated
    @property
    def is_active(self):
        return self.__is_authenticated
    @property
    def is_anonymous(self):
        return self.__is_anonymous
    