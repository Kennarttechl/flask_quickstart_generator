USER_MODEL = """
from sqlalchemy.sql import func
from flask_login import UserMixin
from flask_login import UserMixin
from my_demo_app import db, login_manager


# This function is used by Flask-Login to load the user from the database.
@login_manager.user_loader
def load_user(user_id):
    # Retrieves a User object based on the user_id (primary key).
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):  # We assume a User can be a Teacher, Administrator
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(length=50), nullable=True)
    email = db.Column(db.String(length=100), unique=True, nullable=True)
    password = db.Column(db.String(length=50), nullable=False)
    user_role = db.Column(db.String(length=50), nullable=False)
    user_profile = db.Column(
        db.String(length=100), nullable=False, default="default.jpg"
    )
    date_created = db.Column(db.Date, default=func.current_date(), nullable=False)

    def __repr__(self) -> str:
        return f"User('{self.username}')"
"""
