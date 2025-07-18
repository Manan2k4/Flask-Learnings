from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from myapp.models import User, Role, db

bp = Blueprint('auth', __name__)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    if request.method == "POST":
        user = User.query.filter_by(email=request.form['email']).first()
        if user:
            msg = 'User already exists'
            return render_template('signup.html', msg=msg)
        
        hashed_password = generate_password_hash(request.form['password'])
        user = User(email=request.form['email'], password=hashed_password)
        role = Role.query.filter_by(id=int(request.form['Options'])).first()
        if role:
            user.roles.append(role)
        else:
            msg = "Invalid role Selection"
            return render_template('signup.html', msg=msg)
        
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('main.index'))
    return render_template('signup.html', msg=msg)

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    msg = ''
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.verify_password(request.form['password']):
            login_user(user)
            return redirect(url_for('main.index'))
        msg = 'Wrong password' if user else "User doesn't exist"
    return render_template('signin.html', msg=msg)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))