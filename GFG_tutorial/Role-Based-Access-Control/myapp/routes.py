from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from flask_security import roles_accepted
from myapp.models import User, Role, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')