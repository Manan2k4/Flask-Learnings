from flask import Blueprint, render_template
from flask_security import roles_accepted
from myapp.models import db, roles_users, User

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/teachers')
@roles_accepted('Admin')
def teachers():
    teachers_list = []
    role_teachers = db.session.query(roles_users).filter_by(role_id=2).all()
    for teacher in role_teachers:
        user = User.query.filter_by(id=teacher.user_id).first()
        if user:
            teachers_list.append(user)
    return render_template('teachers.html', teachers=teachers_list)

@admin_bp.route('/staff')
@roles_accepted('Admin', 'Teacher')
def staff():
    staff_list = []
    role_staff = db.session.query(roles_users).filter_by(role_id=3).all()
    for s in role_staff:
        user = User.query.filter_by(id=s.user_id).first()
        if user:
            staff_list.append(user)
    return render_template('staff.html', staff=staff_list)

@admin_bp.route('/students')
@roles_accepted('Admin', 'Teacher', 'Staff', 'Student')
def students():
    return render_template('mydetails.html')