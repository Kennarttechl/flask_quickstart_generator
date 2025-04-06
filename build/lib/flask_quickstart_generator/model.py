USER_MODEL = """

from sqlalchemy.sql import func
from flask_login import UserMixin
from my_demo_app import db, login_manager


# This function is used by Flask-Login to load the user from the database.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):  # We assume a User can be a Teacher, Administrator
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    username = db.Column(db.String(length=150), nullable=True)   
    password = db.Column(db.String(length=255), nullable=False)  
    user_role = db.Column(db.String(length=100), nullable=False)  
    user_profile = db.Column(
        db.String(length=200), nullable=False, default="default.jpg" 
    )
    date_created = db.Column(db.Date, default=func.current_date(), nullable=False)
    
    __table_args__ = (
        db.Index('user_idx', 'date_created'),
    )

    def __repr__(self) -> str:
        return f"User('{self.username}')"


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Role('{self.name}')"
"""
