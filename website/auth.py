from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "<h1>Login</h1>"

@auth.route("/logout")
def logout():
    return "<h1>LogOut</h1>"

@auth.route("/signup")
def signUp():
    return "<h1>SignUp</h1>"
