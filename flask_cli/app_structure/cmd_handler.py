import os
from flask_cli.app_template.html import BASE_HTML, DEMO_HTML


APP_SETTINGS = """
import os
import secrets 
from flask_migrate import Migrate
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect


# Create a Flask application instance
app = Flask(__name__)


# SECURITY WARNING: keep the secret key used in production secret!
# Use a secure environment variable to store the secret key.
# You can use the 'secrets' module (available in Python 3.6+) to generate a secret key:
SECRET_KEY = 'flask-insecure-c#y(k55srf&7q^i@mi+f*tw_%ll$^w@#cd1=fwa6&8tr^2qwv1'
secret_key = secrets.token_urlsafe(20) # Generate a secure secret key


# Define the database path relative to the application directory 
APP_DATABASE = os.path.join(os.path.dirname(__file__), "database")
DATABASE_PATH = os.path.join(APP_DATABASE, "Database.db") # Database name can be change


# Configure Flask application settings
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# Initialize database, CSRF protection, and migration management instances
db = SQLAlchemy(app)
csrf = CSRFProtect(app) # Protect against Cross-Site Request Forgery (CSRF) attacks
migrate = Migrate(app, db) # Database migration with Flask-Migrate


# Configure Flask-Session for database-backed sessions
app.config['SESSION_TYPE'] = 'sqlalchemy'  # Use SQLAlchemy backend
app.config['SESSION_SQLALCHEMY'] = db  # Reference SQLAlchemy instance
app.config['SESSION_SQLALCHEMY_TABLE'] = "flask_sessions"  # Use the Session model
app.config['SESSION_PERMANENT'] = False  # Set to True for persistent sessions
app.config['SESSION_USE_SIGNER'] = True  # Use a secret key for signing

Session(app)  # Initialize Flask-Session extension


@app.before_request
def app_middleware():
    #This middleware function performs several actions before each request:

    # URL Canonicalization: Redirects URLs with uppercase letters to lowercase for consistent URL handling.
    
    # Trailing Slash Removal: Removes trailing slashes from URLs except for the root URL, promoting cleaner URLs.

    # URL Canonicalization: Redirect URLs with uppercase letters to lowercase
    if request.path != request.path.lower():
        return redirect(request.path.lower())

    # Remove trailing slashes except for root URL
    if request.path != '/' and request.path.endswith('/'):
        return redirect(request.path.rstrip('/'))


@app.after_request
def app_security_headers_middleware(response):
    #This middleware function sets the X-Frame-Options header to "DENY" to prevent clickjacking attacks.
    
    # Security Headers: Sets essential security headers to mitigate potential vulnerabilities:
    
    # Referrer-Policy: Limits referrer information leaks.
    
    # X-Content-Type-Options: Prevents MIME-sniffing.
    
    # Content-Security-Policy (Basic implementation): Provides a starting point for restricting resource loading.
    
    # X-Frame-Options: # Prevent clickjacking
    
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

    response.headers["X-Content-Type-Options"] = "nosniff"
    
    response.headers["Content-Security-Policy"] = "default-src 'self'"

    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' https://cdn.example.com https://cdnjs.cloudflare.com; "
        "style-src 'self' https://cdn.example.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' https://cdn.example.com data;"
    )

    response.headers["X-Frame-Options"] = "DENY" # Prevent clickjacking

    return response
    
    
# Import and register blueprint containing application routes
from my_demo_app.views.routes import view
from my_demo_app.errors.handler import errors_
from my_demo_app.authentication.authent import authent_


app.register_blueprint(view, url_prefix="/")
app.register_blueprint(errors_, url_prefix="/")
app.register_blueprint(authent_, url_prefix="/")
"""


APP_SESSION = \
"""
from my_demo_app import db



class Session(db.Model):
    __tablename__ = 'sessions'  # Customize table name if desired

    session_id = db.Column(db.String(255), primary_key=True, unique=True)
    session_data = db.Column(db.Text)  # Store session data as serialized JSON
    expiration_time = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return f"Session('{self.session_id}')"
    
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
static_url_path="static")


@view.route("/")
def home_page():
    return render_template("index.html")
"""


ERROR_HANDLER_TEMPLATE_CODE = """
from http import HTTPStatus
from flask import render_template, Blueprint


errors_ = Blueprint("errors_", __name__, template_folder="templates", static_url_path="static")


@errors_.app_errorhandler(403)
def error_403(error):
    return render_template("error_403.html"), HTTPStatus.FORBIDDEN


@errors_.app_errorhandler(404)
def error_404(error):
    return render_template("error_404.html"), HTTPStatus.NOT_FOUND
    

@errors_.app_errorhandler(500)
def error_500(error):
    return render_template("error_500.html"), HTTPStatus.INTERNAL_SERVER_ERROR

"""


AUTHENTICATION_TEMPLATE_CODE = """
from flask import render_template, Blueprint


authent_ = Blueprint("authent_", __name__, template_folder="templates", static_url_path="static")


@authent_.route("/")
def demo_page():
    return render_template("authent.html")
"""

GITIGNORE = """
*.db
venv/
config/.venv
**/*/__pycache__
"""
    

APP_STRUCTURE = {
    "templates": {
        "base.html": BASE_HTML, 
        "index.html": DEMO_HTML
        },
    
    "views": {
        "routes.py": VIEW_TEMPLATE_CODE, 
        "__init__.py": ""
        },
    
    "errors": {
        "handler.py": ERROR_HANDLER_TEMPLATE_CODE,
        "__init__.py": "",
    },
    
    "authentication":{
      "authent.py": AUTHENTICATION_TEMPLATE_CODE,
      "__init__.py": ""  
    },

    "static": {
        "css": "style.css", 
        "js": "script.js", 
        "images": "flask_cli.png",
        },
    
    "database": {
        "models.py": APP_SESSION, 
        "__init__.py": ""
        },
    
    "config":{
        ".env": "",
        ".flaskenv": ""
    }
}


# ANSI escape color code for displaying or printing sucessful message
GREEN = '\033[92m'
RESET = '\033[0m'


#ANSI escape color code for displaying or printing sucessful message
YELLOW = "\033[33m"
RESET = "\033[0m"


class CmdHandler():

    def init():
        print(f"{GREEN}Please wait, app is setting up virtual environment......{RESET}")
        os.system("pip install virtualenv && virtualenv env")
        print(f"{GREEN}Please wait installing, Flask, Flask-Session, Flask-SQLAlchemy and Flask-Migrate{RESET}")
        os.system("pip install Flask Flask-Session Flask-SQLAlchemy Flask-Migrate")

    # @staticmethod
    def create_flask_app_structure(app_folder_name):
        try:
            if not os.path.exists(app_folder_name):
                os.mkdir(app_folder_name)
                with open(file="app.py", mode="w") as file:
                    file.write(APP_STARTUP.replace("my_demo_app",  app_folder_name))

                with open(file=f"{app_folder_name}/__init__.py", mode="w") as file:
                    file.write(APP_SETTINGS.replace("my_demo_app", app_folder_name))
                
                with open(file=f"{app_folder_name}/.gitignore", mode="w") as file:
                    file.write(GITIGNORE)

                for dir, content in APP_STRUCTURE.items():
                    os.mkdir(os.path.join(app_folder_name, dir))
                    
                    if dir in ["errors", "views", "authentication"]:
                        os.mkdir(os.path.join(app_folder_name, dir, "templates"))

                    if dir in ["static"]:
                        for static_dir, value in content.items():
                            os.makedirs(os.path.join(app_folder_name, dir, static_dir))
                            with open(
                                os.path.join(app_folder_name, dir, static_dir, value), mode="w"
                            ) as file:
                                file.write("")

                    if dir in ["templates", "views", "errors", "authentication", "database", "config"]:
                        for temp, value in content.items():
                            with open(os.path.join(app_folder_name, dir, temp), mode="w") as file:
                                file.write(value.replace("my_demo_app", app_folder_name))
            else:
                print(f"{YELLOW} The Folder {app_folder_name} already exists. {RESET}")
        except FileExistsError as e:
            print(f"{YELLOW} Error: {e}{RESET}")
        