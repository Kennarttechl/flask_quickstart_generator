USER_MODEL = """
from my_demo_app import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class User(db.Model, UserMixin):
    user = db.Column(db.Integer(), primary_key=True, unique=True)
    username = db.Column(db.String(length=50), nullable=True)
    password = db.Column(db.String(length=50), nullable=False)
    confirm_password = db.Column(db.String(50), nullable=False)
    user_role = db.Column(db.String(length=50), nullable=False)
    email = db.Column(db.String(length=100), nullable=True)
    user_profile = db.Column(
        db.String(length=100), nullable=False, default="default.jpg"
    )
    date_created = db.Column(
        db.DateTime(timezone=True), nullable=False, default=func.now()
    )

    def __repr__(self) -> str:
        return f"User('{self.username}')"
"""
