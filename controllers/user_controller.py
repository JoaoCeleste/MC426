from facade import Facade
from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user


class UserController:
    @staticmethod
    def register():
        return Facade.register()

    @staticmethod
    def login():
        return Facade.login()

    @staticmethod
    @login_required
    def logout():
        return Facade.logout()

    @staticmethod
    @login_required
    def home():
        return Facade.home()
