from facade.user_facade import UserFacade
import hashlib

user_facade = UserFacade()


def register():
    return user_facade.register()


def login():
    return user_facade.login()


def logout():
    return user_facade.logout()


def home():
    return user_facade.home()


def config():
    return user_facade.config()


def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


def check_password(password, hashed_password):
    return hash_password(password) == hashed_password
