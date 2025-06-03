from myapp import create_app
from myapp.models import Role
from myapp.db import db

app = create_app()

def create_roles():
    with app.app_context():
        roles = ['Admin', 'Teacher', 'Staff', 'Student']
        for i, name in enumerate(roles, start=1):
            role = Role(id=i, name=name)
            db.session.add(role)
        db.session.commit()
        print("Roles created successfully!")

if __name__ == '__main__':
    create_roles()