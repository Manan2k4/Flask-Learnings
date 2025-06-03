from flask import Blueprint, render_template
from flask_security import roles_accepted
from .models import db, roles_users, User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/teachers')
@roles_accepted('Admin')
def teachers():
    teachers_list = []
    role_teachers = db.session.query(roles_users).filter_by(role_id=2).all()
    for teacher in role_teachers:
        user = User.query.filter_by(id=teacher.user_id).first()
        if user:
            teachers_list.append(user)
    return render_template('teachers.httml', teachers=teachers_list)

@bp.route('/staff')
@roles_accepted('Admin', 'Teacher')
def staff():
    staff_list = []
    role_staff = db.session.query(roles_users).filter_by(role_id=3).all()
    for s in role_staff:
        user = User.query.filter_by(id=s.user_id).first()
        if user:
            staff_list.append(user)
    return render_template('staff.html', staff=staff_list)

@bp.route('/students')
@roles_accepted('Admin', 'Teacher', 'Staff', 'Student')
def mydetails():
    return render_template('mydetails.html')