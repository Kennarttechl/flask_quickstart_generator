GITIGNORE = \
"""
*.db
venv/
config/.venv
__pycache__
/__pycache__
**/*/__pycache__
"""

ANSI_COLORS_ = \
    """ 
import sys
import os

# Custom ANSI escape codes
CUSTOM_COLORS = {
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "YELLOW": "\033[93m",
    "RESET": "\033[0m",
}

# No color fallback
NO_COLOR = {
    "GREEN": "",
    "RED": "",
    "YELLOW": "",
    "RESET": "",
}

def get_color_support():
    # Dynamically returns the best color support depending on the environment.
    # - VS Code => colorama
    # - Sublime Text or others => ANSI (custom)
    # - Fallback => no color
    try:
        # If output is a real terminal
        if sys.stdout.isatty():
            # VS Code specific: has full ANSI + colorama support
            if "VSCODE_PID" in os.environ:
                from colorama import init, Fore, Style

                init(autoreset=True)
                return {
                    "GREEN": Fore.GREEN,
                    "RED": Fore.RED,
                    "YELLOW": Fore.YELLOW,
                    "RESET": Style.RESET_ALL,
                }

            # Other terminals that support ANSI (like CMD, Linux)
            return CUSTOM_COLORS

    except Exception:
        pass

    # Fallback (Sublime Text or broken shell)
    return NO_COLOR
"""


APP_STARTUP = \
"""
from waitress import serve
from my_demo_app import db, app, flask_db_init
from my_demo_app.super_admin.routes import seed_super_admin


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # db.drop_all()
        flask_db_init()  #This function creates and initiates the `db migration folder`
        seed_super_admin()
    app.run(host="0.0.0.0",debug=True, port=5000) 
    # serve(app, host='0.0.0.0', port=5000, threads=100) # Use Waitress to serve the app 
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

@view.route("/")
@view.route("/home_page")
@limiter.limit("5 per minute", override_defaults=True)
def home_page():

    return render_template("index.html")

# @view.route("/")
# @view.route("/home_page", methods=["GET", "POST"])
# @limiter.limit("5 per minute", override_defaults=True)
# def home_page():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             if user.user_role == "SuperAdmin":
#                 login_user(user)
#                 flash(message=f"Login Successfuly {user.username}", category="success")
#                 return redirect(url_for(endpoint="admin_controller.secure_dashboard"))
#             elif user.user_role == "NormalUser":
#                 login_user(user)
#                 flash(message=f"Login Successfuly {user.username}", category="success")
#                 return redirect(url_for(endpoint="admin_controller.secure_dashboard"))
#         else:
#             flash(message="Invalid Username or Password", category="error")
#     return render_template("index.html", form=form)
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
from my_demo_app import app
from flask import session
from http import HTTPStatus
from flask import render_template, Blueprint, flash


errors_ = Blueprint(
    "errors_", __name__, template_folder="templates", static_folder="static"
)

@errors_.app_errorhandler(400)
def bad_request(error):
    return render_template("bad_request.html"), HTTPStatus.BAD_REQUEST


@errors_.app_errorhandler(401)
def un_authorized(error):
    return render_template("unauthorized.html"), HTTPStatus.UNAUTHORIZED


@errors_.app_errorhandler(403)
def forbidden_error(error):
    return render_template("forbidden.html"), HTTPStatus.FORBIDDEN


@errors_.app_errorhandler(404)
def not_found_error(error):
    return render_template("not_found.html"), HTTPStatus.NOT_FOUND


@errors_.app_errorhandler(413)
def payload_too_large_error(error):
    return render_template("payload_data.html"), HTTPStatus.CONTENT_TOO_LARGE


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

AUTHENTICATION_TEMPLATE_CODE = \
"""
from .form import RegisterForm
from my_demo_app.database.models import Role, User
from my_demo_app import limiter, bcrypt, db, logging
from flask_login import current_user, logout_user, login_required
from flask import render_template, Blueprint, flash, redirect, url_for


authent_ = Blueprint(
    "authent_", __name__, template_folder="templates", static_folder="static"
)


@authent_.route(rule="/reguser", methods=["GET", "POST"])
@limiter.limit("5 per minute", override_defaults=True)
@login_required
def secure_register():
    # Check if any roles exist
    if not Role.query.first():
        flash(
            message="No user roles found! Please add roles before registering users.",
            category="error",
        )
        return redirect(url_for("super_admin_secure.add_role"))  # Redirect admin to add roles

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
            return redirect(url_for(endpoint="super_admin_secure.secure_adashboard"))
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
            message=f"Registration Unsuccessful! {', '.join(error_messages)}",
            category="error",
        )
    image_file = url_for("static", filename="media/" + current_user.user_profile)
    return render_template("signup.html", form=form, image_file=image_file)


# @authent_.route("/logout")
# def user_logout():
#     logout_user()
#     flash(message="Logout Successfully", category="success")
#     return redirect(url_for("view.home_page"))
"""

ACCOUNT_UTILS = \
""" 
import os
import secrets
from my_demo_app import app
from PIL import Image
from flask import Blueprint
from flask_login import current_user
from werkzeug.utils import secure_filename


img_utils = Blueprint(
    "img_utils", __name__, template_folder="templates", static_folder="static"
)


def save_user_picture(form_picture):
    # Generate a random hexadecimal name
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    
    # Sanitize the filename using secure_filename
    picture_fn = secure_filename(random_hex + f_ext)
    
    # Define the picture path
    picture_path = os.path.join(
        app.root_path, "static/media", picture_fn
    )
    
    # Remove the existing user profile picture if it exists
    if os.path.exists(
        os.path.join(app.root_path, "static/media", current_user.user_profile)):
        os.remove(os.path.join(app.root_path, "static/media", current_user.user_profile))
    
    # Resize the image
    output_size = (750, 750)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn
"""

ACCOUNT_SETTINGS_TEMPLATE_CODE = \
"""
from my_demo_app import db, bcrypt
from .form import UpdateAccount
from my_demo_app.media_utils.utils import save_user_picture
from flask_login import current_user, login_required
from flask import render_template, Blueprint, request, redirect, flash, url_for


account_ = Blueprint(
    "account_", __name__, template_folder="templates", static_folder="static"
)


@account_.route(rule=f"/account", methods=["GET", "POST"])
@login_required
def secure_account_update():
    form = UpdateAccount()

    if form.validate_on_submit():
        # Handle profile picture update if provided
        if form.picture.data:
            picture_file = save_user_picture(form.picture.data)
            current_user.user_profile = picture_file

        # Handle username update
        current_user.email = form.email.data
        current_user.username = form.username.data

        # Handle password update only if a new password is provided
        if form.password.data:
            # Check if passwords match
            if form.password.data == form.confirm_password.data:
                # Hash the new password and update it
                hashed_password = bcrypt.generate_password_hash(
                    form.password.data
                ).decode("utf-8")
                current_user.password = hashed_password
            else:
                flash(message="Passwords do not match.", category="error")
                return redirect(url_for(endpoint="account_.secure_account_update"))

        # Commit the changes to the database
        db.session.commit()
        flash(message="Your account has been updated!", category="success")
        return redirect(url_for(endpoint="super_admin_secure.secure_adashboard"))

    # If validation fails, flash the errors for debugging
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(message=f"Error in {field}: {error}", category="error")

    # Prepopulate fields for GET request
    elif request.method == "GET":
        form.email.data = current_user.email
        form.username.data = current_user.username

    image_file = url_for("static", filename="media/" + current_user.user_profile)

    return render_template(
        template_name_or_list="update_account.html", image_file=image_file, form=form
    )
"""

FILES_UPLOAD_TEMPLATE_CODE = \
""" 
import os
from my_demo_app import limiter, app, cache
from werkzeug.utils import secure_filename
from .form import MultipleFileUploadForm, SingleFileUploadForm
from flask import render_template, Blueprint, redirect, url_for


file_upload_ = Blueprint(
    "file_upload_", __name__, template_folder="templates", static_folder="static"
)


# Route for handling single file upload
@file_upload_.route("/singleupload", methods=["GET", "POST"])
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

SUPER_ADMIN_DASHBOARD_ = \
""" 
import os
from my_demo_app import limiter
from dotenv import load_dotenv
from .form import LoginForm, RoleForm
from my_demo_app import db, bcrypt, app, logging
from my_demo_app.database.models import User, Role
from flask_login import current_user, login_required, login_user, logout_user
from flask import render_template, session, url_for, flash, redirect, Blueprint


super_admin_secure = Blueprint(
    import_name=__name__,
    name="super_admin_secure",
    template_folder="templates",
    static_folder="static",
)


load_dotenv(dotenv_path="my_demo_app/config/.env")
admin_username = os.getenv("ADMIN_USERNAME")
admin_password = os.getenv("ADMIN_PASSWORD")


def seed_super_admin():
    # Check if the admin user already exists
    existing_admin = User.query.filter_by(email="admin@example.com").first()
    if existing_admin:
        # Admin user already exists, no need to add again
        return

    # If the admin doesn't exist, create it
    admin = User(
        username=admin_username,
        password=bcrypt.generate_password_hash(admin_password).decode("utf-8"),
        user_role="SuperUser",
        email="admin@example.com",
        user_profile="default.jpg",
    )
    db.session.add(admin)
    db.session.commit()


@super_admin_secure.route(rule="/superlogin", methods=["GET", "POST"])
@limiter.limit(limit_value="5 per minute", override_defaults=True)
def secure_superlogin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(message=f"Login Successfuly {user.username}", category="success")
            return redirect(url_for(endpoint="super_admin_secure.secure_adashboard"))
        else:
            flash(message="Invalid Username or Password", category="error")
    return render_template("salogin_secure.html", form=form)


@super_admin_secure.route(rule="/secure_adashboard", methods=["GET", "POST"])
@limiter.limit(limit_value="5 per minute", override_defaults=True)
@login_required
def secure_adashboard():
    image_file = url_for("static", filename="media/" + current_user.user_profile)
    return render_template("sadashboard_secure.html", image_file=image_file)


@super_admin_secure.route(rule="/user_role", methods=["GET", "POST"])
@login_required
def add_role():
    form = RoleForm()
    if form.validate_on_submit():
        try:
            # Check if the role already exists before adding it
            existing_role = Role.query.filter_by(name=form.role_name.data).first()
            if existing_role:
                flash(message="Role already exists! choose different role", category="error")
                return redirect(url_for("super_admin_secure.add_role"))

            # Create a new role
            roles = Role(name=form.role_name.data)
            db.session.add(roles)
            db.session.commit()

            flash(message="User role added successfully", category="success")
            return redirect(url_for(endpoint="super_admin_secure.secure_adashboard"))

        except Exception as e:
            db.session.rollback()
            logging.error(f"Error adding User Roles: {str(e)}")
            flash(
                message="There was a problem adding User Role to the database",
                category="error",
            )

    # If form errors exist, flash the error messages
    if form.errors:
        error_message = [
            err_msg for err_msg_list in form.errors.values() for err_msg in err_msg_list
        ]
        flash(
            message=f"There was a problem with the form submission: {'. '.join(error_message)}",
            category="error",
        )
    image_file = url_for("static", filename="media/" + current_user.user_profile)
    return render_template("user_role.html", form=form, image_file=image_file)



@super_admin_secure.route("/logout")
def user_logout():
    logout_user()  # Logs out the user
    flash(message="Logout Successfully", category="success")
    return redirect(url_for("super_admin_secure.secure_superlogin"))
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