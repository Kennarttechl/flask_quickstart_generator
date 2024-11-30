GITIGNORE = \
"""
*.db
venv/
config/.venv
__pycache__
/__pycache__
**/*/__pycache__
"""


APP_STARTUP = \
"""
from my_demo_app import db, app, flask_db_init


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # db.drop_all()  
        flask_db_init()  # This function creates and initiates the `db migration`
    app.run(debug=True, port=5000)
"""


VIEW_TEMPLATE_CODE = \
"""
from flask_login import login_user
from flask import flash, redirect, url_for
from my_demo_app import limiter, bcrypt, db
from my_demo_app.database.models import User
from flask import render_template, Blueprint
from my_demo_app.authentication.form import LoginForm


view = Blueprint("view", __name__, template_folder="templates", static_folder="static")


@view.route("/", methods=["GET", "POST"])
@limiter.limit("5 per minute", override_defaults=True)
def home_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            if user.user_role == "SuperAdmin":
                login_user(user)
                flash(message=f"Login Successfuly {user.username}", category="success")
                return redirect(url_for(endpoint="admin_controller.secure_dashboard"))
            elif user.user_role == "NormalUser":
                login_user(user)
                flash(message=f"Login Successfuly {user.username}", category="success")
                return redirect(url_for(endpoint="admin_controller.secure_dashboard"))
        else:
            flash(message="Invalid Username or Password", category="error")
    return render_template("index.html", form=form)
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


SEARCH_TEMPLATE_CODE = \
"""
from sqlalchemy import or_
from my_demo_app import limiter
from .form import ProductSearchForm
from my_demo_app.database.models import User
from flask import render_template, Blueprint, flash


search_ = Blueprint(
    "search_", __name__, template_folder="templates", static_folder="static"
)


@search_.route("/search")
@limiter.limit("5 per minute", override_defaults=True)
def search_item():
    form = ProductSearchForm()
    search_results = []  # Intialize early to avoid UnboundLocalError

    if form.validate_on_submit():
        search_query = form.search_query.data
        search_results = User.query.filter(
            User.username.ilike(f"%{search_query}%")
        ).all()
        if search_results:
            flash(
                message=f"{len(search_query)}Data found for query: {search_query}",
                category="success",
            )
        else:
            flash(message=f"Data not found for query: {search_query}", category="error")
    return render_template("item_search.html", form=form, search_results=search_results)
"""


ERROR_HANDLER_TEMPLATE_CODE = \
"""
from flask import session
from my_demo_app import app
from http import HTTPStatus
from flask import render_template, Blueprint, flash


errors_ = Blueprint(
    "errors_", __name__, template_folder="templates", static_folder="static"
)


@errors_.app_errorhandler(403)
def forbidden_error(error):
    return render_template("forbidden.html"), HTTPStatus.FORBIDDEN


@errors_.app_errorhandler(404)
def not_found_error(error):
    return render_template("not_found.html"), HTTPStatus.NOT_FOUND


@errors_.app_errorhandler(413)
def payload_too_large_error(error):
    return render_template("payload_data.html"), HTTPStatus.PAYLOAD_TOO_LARGE


@errors_.app_errorhandler(429)
def too_many_requests_error(error):
    flash(
        message="Your request is too much, try again in a few minutes", category="error"
    )
    return render_template("too_many_requests.html"), HTTPStatus.TOO_MANY_REQUESTS


@errors_.app_errorhandler(500)
def internal_server_error(error):
    return (
        render_template("internal_server.html"),
        HTTPStatus.INTERNAL_SERVER_ERROR,
    )


@errors_.app_errorhandler(ValueError)
def value_error(error):
    error_message = session.pop("error_message", None)
    if error_message:
        app.logger.error(error_message)
    else:
        app.logger.error(f"Error occurred: {error}")
    return render_template("invalid_path.html")


def maintainance():
    # Your logic here
    pass


@errors_.app_errorhandler(503)
def app_maintenance_mode(error):  # Optional prefix for consistency
    if maintainance:  # Replace with your logic to check maintenance mode
        return render_template("maintenance.html"), HTTPStatus.SERVICE_UNAVAILABLE
    # Code to handle other 503 errors (optional)
    return None  # Fallback for non-maintenance related 503 errors

"""


AUTHENTICATION_FORM = \
""" 
from flask_wtf import FlaskForm
from my_demo_app.database.models import User
from wtforms import SubmitField, StringField, PasswordField, SelectField, EmailField
from wtforms.validators import (
    Length,
    EqualTo,
    DataRequired,
    InputRequired,
    ValidationError,
)


class RegisterForm(FlaskForm):
    # Registration form for creating new user accounts.

    username = StringField(
        validators=[DataRequired(), Length(min=4, max=15)],
        render_kw={"placeholder": "Username"},
    )
    
    email = EmailField(
        validators=[DataRequired(), Length(max=100)],
        render_kw={"placeholder": "Email"},)
    
    password = PasswordField(
        validators=[DataRequired(message="Enter password"), Length(min=4, max=15)],
        render_kw={"placeholder": "Password"},
    )

    confirm_password = PasswordField(
        validators=[InputRequired(), EqualTo("password", message="Password must much")],
        render_kw={"placeholder": "Repeat Password"},
    )

    user_role = SelectField(
        validators=[DataRequired()],
        choices=[
            ("", "Select Role"),
            ("NormalUser", "NormalUser"),
            ("SuperAdmin", "SuperAdmin"),
        ],
        coerce=str,
        default="",
    )

    register = SubmitField(label="Register")
    

    def validate_username(self, username):
        '''
        Custom validation function to check for existing username.
        Raises a ValidationError if the username already exists in the database.
        '''
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(message="Username already exist!")

    def validate_email(self, email):
        '''
        Custom validation function to check for existing email.
        Raises a ValidationError if the email already exists in the database.
        '''
        
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(message="Email already exists!")

    def validate_user_role(self, user_role):
        '''
        Custom validation function to ensure a valid user role is selected.
        Raises a ValidationError if the selected role is invalid or already exists.
        '''

        if user_role.data == "":
            raise ValidationError(message="Please select a valid user role.")

        existing_user = User.query.filter_by(user_role=user_role.data).first()
        if existing_user:
            raise ValidationError(message="User role already exists!")


class LoginForm(FlaskForm):
    # Login form for authenticating existing user accounts.

    username = StringField(
        validators=[DataRequired()], render_kw={"placeholder": "Username"}
    )

    password = PasswordField(
        validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )

    loginb_ = SubmitField(label="Submit")
"""


AUTHENTICATION_TEMPLATE_CODE = \
"""
import secrets
from .form import RegisterForm
from flask_login import logout_user
from my_demo_app.database.models import User
from my_demo_app import limiter, bcrypt, db, logging
from flask import render_template, Blueprint, flash, redirect, url_for


authent_ = Blueprint(
    "authent_", __name__, template_folder="templates", static_folder="static"
)


@authent_.route("/reguser", methods=["GET", "POST"])
@limiter.limit("5 per minute", override_defaults=True)
# @login_required
def secure_register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            pw_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=pw_hash,
                user_role=form.user_role.data,
            )
            db.session.add(user)
            db.session.commit()
            flash(
                message=f"Account Created Successfully {user.username}",
                category="success",
            )
            return redirect(url_for(endpoint="admin_controller.secure_dashboard"))
        except Exception as e:
            db.session.rollback()
            logging.error(msg=f"Error adding new user to the database {e}")
            flash(
                message="There was a problem adding data to the database",
                category="error",
            )

    error_messages = [
        err_msg for err_msg_list in form.errors.values() for err_msg in err_msg_list
    ]
    if error_messages:
        flash(
            message=f"Registration Unsuccessfull! {', '.join(error_messages)}",
            category="error",
        )
    return render_template("signup.html", form=form)


@authent_.route("/logout")
def user_logout():
    logout_user()
    flash(message="Logout Successfully", category="success")
    return redirect(url_for("view.home_page"))
"""


ACCOUNT_UTILS = \
""" 
import os
import secrets
from PIL import Image
from my_demo_app import app
from flask import Blueprint
from flask_login import current_user


img_utils = Blueprint(
    "img_utils", __name__, template_folder="templates", static_folder="static"
)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, "static/profile_pics", picture_fn
    )  # app.
    if os.path.exists(
        app.root_path + "/static/media/" + current_user.user_profile
    ):
        os.remove(app.root_path + "/static/media/" + current_user.user_profile)

    output_size = (100, 100)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
"""


ACCOUNT_SETTINGS_FORM = \
""" 
from flask_wtf import FlaskForm
from flask_login import current_user
from my_demo_app.database.models import User
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, ValidationError


class UpdateAccount(FlaskForm):
    username = StringField(validators=[DataRequired()])
    picture = FileField(
        label="Update account profile", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField(label="Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    "That username already exist! Please try a different username"
                )
"""


ACCOUNT_SETTINGS_TEMPLATE_CODE = \
"""
import secrets
from my_demo_app import db
from .form import UpdateAccount
from flask import render_template, Blueprint


account_ = Blueprint(
    "account_", __name__, template_folder="templates", static_folder="static"
)


#@account_.route(f"/{secrets.token_urlsafe()}")
@account_.route("/reset", methods=["GET"])
def secure_password():
    return render_template("reset_pswd.html")


@account_.route(f"/{secrets.token_urlsafe()}")
def secure_account_update():
    return render_template("update_account.html")
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


FILES_UPLOAD_TEMPLATE_CODE = \
""" 
import os
import secrets
from my_demo_app import limiter, app, cache
from werkzeug.utils import secure_filename
from .form import MultipleFileUploadForm, SingleFileUploadForm
from flask import render_template, Blueprint, redirect, url_for


file_upload_ = Blueprint(
    "file_upload_", __name__, template_folder="templates", static_folder="static"
)


# Route for handling single file upload
@file_upload_.route(f"/{secrets.token_urlsafe()}", methods=["GET", "POST"])
#@file_upload_.route("/singleupload", methods=["GET", "POST"])
@limiter.limit("10 per minute", override_defaults=True)
def secure_single_upload():
    # Create form instance
    form = SingleFileUploadForm()

    # Check if form is submitted and valid
    if form.validate_on_submit():
        # Access the uploaded file
        file = form.file.data

        # Check if a file was uploaded
        if file:
            # Get file extension and lowercase it
            extension = os.path.splitext(file.filename)[1].lower()

            # Generate secure file path
            file_path = os.path.join(
                app.config["UPLOAD_FOLDER"], secure_filename(file.filename)
            )

            # Check if file extension is allowed
            if extension not in app.config["ALLOWED_EXTENSIONS"]:
                return "File is not an allowed type"

            # Save the file to the upload folder
            file.save(file_path)
            
            # Invalidate the cache for the homepage
            with app.app_context():
                cache.delete("home_page")

            # Redirect to registration page after successful upload
            return redirect(url_for("view.home_page"))
        else:
            # Inform user if no file was selected
            return "No file selected"

    # Render the template with the form
    return render_template("file_upload.html", form=form)


# Route for handling multiple file uploads
# @file_upload_.route("/multiple_upload", methods=["GET", "POST"])
# @limiter.limit("10 per minute", override_defaults=True)
# def secure_multiple_upload():
#     # Create form instance
#     form = MultipleFileUploadForm()

#     # Check if form is submitted and valid
#     if form.validate_on_submit():
#         # Access uploaded files as a list
#         files = form.files_.data

#         # Check if any files were uploaded
#         if files:
#             # Loop through each uploaded file
#             for file in files:
#                 # Get file extension and lowercase it
#                 extension = os.path.splitext(file.filename)[1].lower()

#                 # Generate secure file path
#                 file_path = os.path.join(
#                     app.config["UPLOAD_FOLDER"], secure_filename(file.filename)
#                 )

#                 # Check if file extension is allowed
#                 if extension not in app.config["ALLOWED_EXTENSIONS"]:
#                     return "File is not an allowed type"

#                 # Save the file to the upload folder
#                 file.save(file_path)

#             # Redirect to registration page after successful upload
#             return redirect(url_for("view.home_page"))
#         else:
#             # Inform user if no files were selected
#             return "No files selected"

#     # Render the template with the form
#     return render_template("file_upload.html", form=form)

"""


ADMIN_TEMPLATE_CODE = \
"""
import secrets
from flask import render_template, Blueprint


admin_controller = Blueprint(
    "admin_controller", __name__, template_folder="templates", static_folder="static"
)
                              

# @admin_controller.route(f"/{secrets.token_urlsafe()}")
@admin_controller.route("/controller", methods=["GET"])
def controller():
    return render_template("controller.html")
"""


CACHING_CONSTANT = \
""" 
from flask import Blueprint


app_cache = Blueprint("app_cache", __name__)


# Constants for minutes
ONE_MINUTE = 60  # 1 minute in seconds
TWO_MINUTES = 2 * ONE_MINUTE  # 2 minutes in seconds
THREE_MINUTES = 3 * ONE_MINUTE  # 3 minutes in seconds
FOUR_MINUTES = 4 * ONE_MINUTE  # 4 minutes in seconds
SIX_MINUTES = 6 * ONE_MINUTE  # 6 minutes in seconds
SEVEN_MINUTES = 7 * ONE_MINUTE  # 7 minutes in seconds
EIGHT_MINUTES = 8 * ONE_MINUTE  # 8 minutes in seconds
NINE_MINUTES = 9 * ONE_MINUTE  # 9 minutes in seconds
TEN_MINUTES = 10 * ONE_MINUTE  # 10 minutes in seconds
ELEVEN_MINUTES = 11 * ONE_MINUTE  # 11 minutes in seconds
TWELVE_MINUTES = 12 * ONE_MINUTE  # 12 minutes in seconds
THIRTEEN_MINUTES = 13 * ONE_MINUTE  # 13 minutes in seconds
FOURTEEN_MINUTES = 14 * ONE_MINUTE  # 14 minutes in seconds


# Constants for days
ONE_DAY = 24 * 60 * 60  # 1 day in seconds
TWO_DAYS = 2 * ONE_DAY  # 2 days in seconds
THREE_DAYS = 3 * ONE_DAY  # 3 days in seconds
FOUR_DAYS = 4 * ONE_DAY  # 4 days in seconds
FIVE_DAYS = 5 * ONE_DAY  # 5 days in seconds
SIX_DAYS = 6 * ONE_DAY  # 6 days in seconds
SEVEN_DAYS = ONE_DAY * 7 # 1 week in seconds
"""