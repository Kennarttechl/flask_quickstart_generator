GITIGNORE = """
*.db
venv/
config/.venv
__pycache__
/__pycache__
**/*/__pycache__
"""


APP_STARTUP = """
from my_demo_app import db, app



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # db.drop_all()    
    app.run(debug=True, port=5000)
"""


VIEW_TEMPLATE_CODE = """
from flask import render_template, Blueprint




view = Blueprint("view", __name__, template_folder="templates", 
static_folder="static")


@view.route("/")
def home_page():
    return render_template("index.html")
"""


SEARCH_FORM_DATA = """ 
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SearchField, SubmitField


class ProductSearchForm(FlaskForm):
    search_query = SearchField(validators=[DataRequired()], render_kw={"placeholder": "Search product name"})
    submit = SubmitField(label="Search")
"""


SEARCH_TEMPLATE_CODE = """
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
    

# @search_.route("/search")
# def search():
#     q = request.args.get("f")
#     if q:
#         result = (
#             User.query.filter(
#                 or_(User.email.ilike(f"%{q}%"), User.date_created.ilike(f"%{q}%"))
#             )
#             .order_by(User.password.asc())
#             .order_by(User.email.desc())
#             .limit(100)
#             .all()
#         )
#     else:
#         result = []
#     return render_template("item_search.html", result=result)
"""


ERROR_HANDLER_TEMPLATE_CODE = """
from http import HTTPStatus
from flask import render_template, Blueprint, flash



errors_ = Blueprint("errors_", __name__, template_folder="templates", static_folder="static")


@errors_.app_errorhandler(403)
def error_403(error):
    return render_template("error_403.html"), HTTPStatus.FORBIDDEN


@errors_.app_errorhandler(404)
def error_404(error):
    return render_template("error_404.html"), HTTPStatus.NOT_FOUND


@errors_.app_errorhandler(429)
def error_429(error):
    flash(message="Your request is too much, try again in a few minute", category="error")
    return render_template("error_429.html"), HTTPStatus.TOO_MANY_REQUESTS
    

@errors_.app_errorhandler(500)
def error_500(error):
    return render_template("error_500.html"), HTTPStatus.INTERNAL_SERVER_ERROR


def maintainance():
    # Your logic here
    pass

@errors_.app_errorhandler(503)
def maintenance_mode(error):
  if maintainance:  # Replace with your logic to check maintenance mode
    return render_template("maintenance.html"), HTTPStatus.SERVICE_UNAVAILABLE
  # Code to handle other 503 errors (optional)
  return None  # Fallback for non-maintenance related 503 errors
"""


AUTHENTICATION_TEMPLATE_CODE = \
"""
import secrets
from college_mgs import limiter
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


ACCOUNT_UTILS = """ 
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


ACCOUNT_SETTINGS_FORM = """ 
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
from college_mgs import db
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


ADMIN_TEMPLATE_CODE = """
import secrets
from flask import render_template, Blueprint


admin_controller = Blueprint(
    "admin_controller", __name__, template_folder="templates", static_folder="static"
)


@admin_controller.route(f"/{secrets.token_urlsafe(nbytes=20)}")
def controller():
    return render_template("controller.html")
"""
