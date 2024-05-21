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
from my_demo_app import db, app


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # db.drop_all()    
    app.run(debug=True, port=5000)
"""


VIEW_TEMPLATE_CODE = \
"""
import os
from my_demo_app import app
from flask import render_template, Blueprint, send_from_directory, abort


view = Blueprint("view", __name__, template_folder="templates", static_folder="static")


@view.route("/")
def home_page():
    # This function retrieves a list of allowed image filenames and renders the homepage template.

    # Get list of all files in the upload folder
    files = os.listdir(app.config["UPLOAD_FOLDER"])

    # Create an empty list to store allowed image filenames
    images = []

    # Loop through each file in the upload folder
    for file in files:
        # Extract the file extension and convert it to lowercase
        extention = os.path.splitext(file)[1].lower()

        # Check if the extension is allowed (e.g., ".jpg", ".png")
        if extention in app.config["ALLOWED_EXTENSIONS"]:
            # If the extension is allowed, add the filename to the images list
            images.append(file)

    # Render the homepage template and pass the list of images
    return render_template("index.html", images=images)


# @view.route("/")
# def home_page():
#     # This function retrieves a list of allowed image filenames using list comprehension and renders the homepage template.

#     # Get list of all files in the upload folder
#     files = os.listdir(app.config["UPLOAD_FOLDER"])

#     # Use list comprehension to filter allowed image filenames based on extension
#     images = [file for file in files if os.path.splitext(file)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
#     ]

#     # Render the homepage template and pass the list of images
#     return render_template("index.html", images=images)


@view.route("/serve-image/<filename>", methods=["GET"])
def serve_image(filename):
    # This function serves an image from the uploads folder based on the provided filename in the URL.

    # Construct the full path to the image file
    image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    # Check if the requested image file exists
    if not os.path.isfile(image_path):

        # Abort the request with a 404 Not Found status code
        abort(404)

    # Use Flask's send_from_directory utility to serve the image
    return send_from_directory(directory=app.config["UPLOAD_FOLDER"], path=filename)
"""


SEARCH_FORM_DATA = \
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


@search_.route("/")
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
from college_mgs import app
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
    return render_template("too_many_requests_error.html"), HTTPStatus.TOO_MANY_REQUESTS


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
import secrets
from my_demo_app import limiter
from flask import render_template, Blueprint


authent_ = Blueprint(
    "authent_", __name__, template_folder="templates", static_folder="static"
)


@authent_.route(f"/{secrets.token_urlsafe()}")
@limiter.limit("5 per minute", override_defaults=True)
def secure_register():
    return render_template("signup.html")


@authent_.route(f"/{secrets.token_urlsafe()}")
@limiter.limit("5 per minute", override_defaults=True)
def secure_login():
    return render_template("login.html")


# route can be define and render without using secrets & limiter module but using it add more robustness to your route and application 
# @authent_.route("/login")
# def secure_login():
#     return render_template("login.html")
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


@account_.route(f"/{secrets.token_urlsafe()}")
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


UPLOAD_FILES_TEMPLATE_CODE = \
""" 
import os
import secrets
from my_demo_app import limiter, app
from werkzeug.utils import secure_filename
from .form import MultipleFileUploadForm, SingleFileUploadForm
from flask import render_template, Blueprint, redirect, url_for


file_upload_ = Blueprint(
    "file_upload_", __name__, template_folder="templates", static_folder="static"
)


# Route for handling single file upload
#@file_upload_.route(f"/{secrets.token_urlsafe()}", methods=["GET", "POST"])
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

            # Redirect to registration page after successful upload
            return redirect(url_for("view.home_page"))
        else:
            # Inform user if no file was selected
            return "No file selected"

    # Render the template with the form
    return render_template("upload.html", form=form)


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
#     return render_template("upload.html", form=form)

"""


ADMIN_TEMPLATE_CODE = \
"""
import secrets
from flask import render_template, Blueprint


admin_controller = Blueprint(
    "admin_controller", __name__, template_folder="templates", static_folder="static"
)


@admin_controller.route(f"/{secrets.token_urlsafe(nbytes=20)}")
def controller():
    return render_template("controller.html")
"""
