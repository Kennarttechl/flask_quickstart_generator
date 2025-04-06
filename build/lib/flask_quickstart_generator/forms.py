SADASHBOARD_FORM = \
"""
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import SubmitField, StringField, PasswordField, EmailField


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()], render_kw={"placeholder": "Email"}) 

    username = StringField(
        validators=[DataRequired()], render_kw={"placeholder": "Username"}
    )
    password = PasswordField(
        validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )
    login = SubmitField(label="Submit")


class RoleForm(FlaskForm):
    # User Role
    role_name = StringField(label=
        "Role Name",
        validators=[DataRequired(), Length(min=3, max=50)],
        render_kw={"placeholder": "Enter Role Name/Number"},
    )
    submit = SubmitField("Add Role")
"""


AUTHENTICATION_FORM = \
""" 
from flask_wtf import FlaskForm
from my_demo_app.database.models import Role, User
from wtforms import SubmitField, StringField, PasswordField, SelectField, EmailField
from wtforms.validators import (
    Length,
    EqualTo,
    DataRequired,
    InputRequired,
    ValidationError,
)


class RegisterForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Fetch roles from the database dynamically
        self.user_role.choices = [("", "Select Role")] + [
            (role.name, role.name) for role in Role.query.all()
        ]

    username = StringField(
        validators=[DataRequired(), Length(min=4, max=15)],
        render_kw={"placeholder": "Username"},
    )

    email = EmailField(
        validators=[DataRequired(), Length(max=100)],
        render_kw={"placeholder": "Email"},
    )

    password = PasswordField(
        validators=[DataRequired(message="Enter password"), Length(min=4, max=15)],
        render_kw={"placeholder": "Password"},
    )

    confirm_password = PasswordField(
        validators=[
            InputRequired(),
            EqualTo("password", message="Password must match"),
        ],
        render_kw={"placeholder": "Repeat Password"},
    )

    user_role = SelectField(
        label="User Role",
        validators=[DataRequired()],
        coerce=str,
        default="",
    )

    register = SubmitField(label="Register")

    def validate_username(self, username):
        # Custom validation function to check for existing username.
        # Raises a ValidationError if the username already exists in the database.
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(message="Username already exist!")

    def validate_email(self, email):
        # Custom validation function to check for existing email.
        # Raises a ValidationError if the email already exists in the database.
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(message="Email already exists!")

    def validate_user_role(self, user_role):
        # Custom validation function to ensure a valid user role is selected.
        # Raises a ValidationError if the selected role is invalid or already exists.
        if user_role.data == "":
            raise ValidationError(message="Please select a valid user role.")

        existing_user = User.query.filter_by(user_role=user_role.data).first()
        if existing_user:
            raise ValidationError(message="User role already exists!")


class LoginForm(FlaskForm):
    username = StringField(
        validators=[DataRequired()], render_kw={"placeholder": "Username"}
    )

    password = PasswordField(
        validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )

    loginb_ = SubmitField(label="Submit")
"""

SEARCH_FORM = \
""" 
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SearchField, SubmitField


class ProductSearchForm(FlaskForm):
    search_query = SearchField(validators=[DataRequired()], render_kw={"placeholder": "Search product name"})
    submit = SubmitField(label="Search")
"""

ACCOUNT_SETTINGS_FORM = \
""" 
from flask_wtf import FlaskForm
from flask_login import current_user
from my_demo_app.database.models import User
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, ValidationError, Optional, Length, EqualTo


class UpdateAccount(FlaskForm):
    email = EmailField(render_kw={"placeholder": "Email"})

    username = StringField(validators=[DataRequired()])

    picture = FileField(validators=[FileAllowed(["jpg", "png"])])

    password = PasswordField(
        validators=[Optional(), Length(min=4, max=15)],
        render_kw={"placeholder": "Password"},
    )

    confirm_password = PasswordField(
        validators=[Optional(), EqualTo("password", message="Passwords must match.")],
        render_kw={"placeholder": "Confirm_Password"},
    )

    submit = SubmitField(label="Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    message="That username already exists! Please choose a different username."
                )
"""

UPLOAD_FILES_FORM = \
""" 
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileField, MultipleFileField, DataRequired


class SingleFileUploadForm(FlaskForm):
    file = FileField(label="Select File", validators=[DataRequired()])
    submit = SubmitField("Submit")


class MultipleFileUploadForm(FlaskForm):
    files_ = MultipleFileField(label="Select files", validators=[DataRequired()])
    submit = SubmitField(label="Submit")
"""