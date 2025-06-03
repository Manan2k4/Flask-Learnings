from myapp import create_app
from myapp.models import Role
from myapp.db import db

app = create_app()

def create_roles():
    with app.app_context():
        roles = ['Admin', 'Teacher', 'Staff', 'Student']
        
        for i, name in enumerate(roles, start=1):
            # Check if role already exists
            existing_role = Role.query.filter_by(id=i).first()
            if not existing_role:
                role = Role(id=i, name=name)
                db.session.add(role)
        
        db.session.commit()
        print("Roles created/verified successfully!")

if __name__ == '__main__':
    create_roles()