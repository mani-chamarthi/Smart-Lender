import os
import sys
from werkzeug.security import generate_password_hash

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from models.user import User

with app.app_context():

    admin_exists = User.query.filter_by(
        email="admin@smartlender.com"
    ).first()

    if admin_exists:
        print("Admin already exists!")

    else:
        admin = User(
            username="admin",
            email="admin@smartlender.com",
            password_hash=generate_password_hash(
                "admin123"
            ),
            role="admin"
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin user created successfully!")