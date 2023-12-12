from models.database import db
from models.user import User
from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user
from facade.user_facade import UserFacade  


user_facade = UserFacade()

def register():
    return user_facade.register()

def login():
    return user_facade.login()

def logout():
    return user_facade.logout()

def home():
    return user_facade.home()
