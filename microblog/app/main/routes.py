from flask import render_template
from flask import Blueprint
from flask_login import login_required, current_user
from app.models import Post
from app.extensions import db

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {'author': {'username': 'John'}, 'body': 'Beautiful day in Portland!'},
        {'author': {'username': 'Susan'}, 'body': 'The Avengers movie was so cool!'}
    ]
    return render_template('index.html', title='Home', posts=posts)