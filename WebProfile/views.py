# importing flask module
from flask import Flask
from flask_htmx import HTMX
from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user, current_user

# FLASK APPLICATION
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


views = Blueprint(__name__, "views")


# LANDING PAGE
@views.route('/')
def profile():
    return render_template("profile.html")



